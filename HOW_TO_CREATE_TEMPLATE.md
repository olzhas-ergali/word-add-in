# 📝 Как создать шаблон Word с переменными

## Способ 1: Через Word UI (простой)

### Шаг 1: Создайте документ в Word

1. Откройте Word
2. Создайте новый документ
3. Напишите текст шаблона

### Шаг 2: Добавьте Content Controls

1. Перейдите: **Разработчик** → **Элементы управления**
   
   *Если вкладка "Разработчик" не видна:*
   - File → Options → Customize Ribbon
   - Поставьте галочку "Developer"

2. Вставьте **Rich Text Content Control** там, где нужна переменная

3. Нажмите **Properties** для каждого control

4. Установите:
   - **Title**: Название переменные (например, "ФИО")
   - **Tag**: UUID переменной (например, `12345678-1234-1234-1234-123456789012`)

### Шаг 3: Сохраните как .docx

Готово! Документ содержит переменные.

---

## Способ 2: Через Open XML SDK (программно)

### Python скрипт для создания шаблона:

```python
from docx import Document
from docx.oxml import OxmlElement
from uuid import uuid4

def add_custom_property(doc, name, value=""):
    """Добавить Custom Property в документ"""
    core_props = doc.core_properties
    # Добавляем кастомное свойство
    # Примечание: python-docx не поддерживает напрямую,
    # нужно использовать python-docx-template или lxml
    pass

def create_template():
    """Создать шаблон Word с переменными"""
    doc = Document()
    
    # Добавляем текст
    doc.add_heading('Договор №{ДОГОВОР_НОМЕР}', 0)
    
    p = doc.add_paragraph('Настоящий договор заключен между ')
    p.add_run('{ФИО_КОНТРАГЕНТА}').bold = True
    p.add_run(' и ')
    p.add_run('{НАША_КОМПАНИЯ}').bold = True
    
    # Генерируем UUID для каждой переменной
    variables = {
        'ДОГОВОР_НОМЕР': str(uuid4()),
        'ФИО_КОНТРАГЕНТА': str(uuid4()),
        'НАША_КОМПАНИЯ': str(uuid4()),
    }
    
    # Сохраняем mapping переменных в комментарий или отдельный файл
    print("Переменные:")
    for name, uid in variables.items():
        print(f"  {name}: {uid}")
    
    # Сохраняем
    doc.save('template.docx')
    
if __name__ == '__main__':
    create_template()
```

Установите:
```bash
pip install python-docx
```

Запустите:
```bash
python create_template.py
```

---

## Способ 3: Использовать существующий API

### Если Printable Forms API уже генерирует шаблоны:

**Ничего делать не нужно!** Ваш код уже поддерживает это:

1. Шаблоны загружаются из API
2. Они уже содержат переменные
3. Add-in их читает и заполняет

### Код уже есть в `pf_api_service.py`:

```python
async def get_pf_document(self, document_id: UUID, token: Optional[str] = None) -> Optional[bytes]:
    """Скачать документ с переменными"""
    url = f"{self.base_url}{settings.printable_forms_get_docx_api}"
    params = {"documentId": str(document_id)}
    
    # ... скачивание ...
    return response.content
```

---

## Способ 4: Интеграция с существующими шаблонами

### Если у вас есть готовые .docx шаблоны:

1. **Загрузите их в Printable Forms систему**
   - Через admin панель
   - Или через API (если есть endpoint для загрузки)

2. **Убедитесь, что переменные правильно именованы**
   - Используйте UUID формат
   - Или специальные маркеры типа `{{variable_name}}`

3. **Настройте маппинг в базе данных Printable Forms**
   - Свяжите переменные с полями БД
   - Укажите откуда брать значения

---

## Формат переменных в Word

### Формат 1: Document Variables (старый способ C#)

```vba
' В Word VBA
ActiveDocument.Variables.Add Name:="VariableName", Value:="InitialValue"
```

Читается в C#:
```csharp
var variables = document.Variables;
string value = variables["VariableName"].Value;
```

### Формат 2: Custom Properties (современный)

Читается в JavaScript:
```javascript
await Word.run(async (context) => {
    const properties = context.document.properties.customProperties;
    properties.load('items');
    await context.sync();
    
    properties.items.forEach(prop => {
        console.log(prop.key, prop.value);
    });
});
```

### Формат 3: Content Controls (рекомендуется для Office.js)

```javascript
await Word.run(async (context) => {
    const controls = context.document.contentControls;
    controls.load('tag, text');
    await context.sync();
    
    controls.items.forEach(control => {
        if (control.tag === 'variable_id') {
            control.insertText('New Value', Word.InsertLocation.replace);
        }
    });
});
```

---

## Пример полного шаблона

### template.docx структура:

```
ДОГОВОР № [VARIABLE:12345678-1234-1234-1234-123456789012]

От [VARIABLE:ABCDEF01-2345-6789-ABCD-EF0123456789]

Контрагент: [VARIABLE:22222222-3333-4444-5555-666666666666]

Сумма: [VARIABLE:33333333-4444-5555-6666-777777777777] руб.
```

### Соответствующая запись в БД:

```json
{
  "documentId": "template-001",
  "variables": [
    {
      "id": "12345678-1234-1234-1234-123456789012",
      "name": "Номер договора",
      "table": "contracts",
      "field": "contract_number"
    },
    {
      "id": "ABCDEF01-2345-6789-ABCD-EF0123456789",
      "name": "Дата",
      "table": "contracts",
      "field": "contract_date"
    }
  ]
}
```

---

## Тестирование шаблона

### Проверьте переменные в Word:

1. Откройте ваш .docx файл
2. Alt+F9 (показать коды полей)
3. Должны быть видны переменные

### Проверьте через Add-in:

1. Загрузите документ в Word
2. Откройте Developer Tools (F12)
3. Выполните:

```javascript
Office.context.document.customXmlParts.getByNamespaceAsync(
    "http://schemas.openxmlformats.org/officeDocument/2006/custom-properties",
    function(result) {
        console.log("Custom properties found:", result.value.length);
    }
);
```

---

## FAQ

### Q: Где хранятся значения переменных?

**A:** В вашей базе данных Printable Forms. API возвращает значения по запросу.

### Q: Можно ли использовать русские имена переменных?

**A:** Да, но UUID надежнее для идентификации.

### Q: Как обновить шаблон?

**A:** Загрузите новую версию через API или admin панель.

### Q: Поддерживаются ли таблицы с переменными?

**A:** Да, можно добавить переменные в ячейки таблиц Word.

---

## Готовые инструменты

### Word Add-in для создания шаблонов:

Можно создать отдельную функцию в вашем Add-in:

```javascript
// В commands.html
async function createTemplate(event) {
    await Word.run(async (context) => {
        const selection = context.document.getSelection();
        
        // Получаем UUID от пользователя
        const variableId = prompt("Введите ID переменной:");
        
        // Создаем Content Control
        const cc = selection.insertContentControl();
        cc.tag = variableId;
        cc.title = "Variable: " + variableId;
        
        await context.sync();
    });
    
    event.completed();
}
```

---

**Итог:** Переменные берутся из Word документов, которые скачиваются из Printable Forms API. Ваш код уже готов для работы с ними! ✅

