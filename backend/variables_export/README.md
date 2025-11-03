# База переменных для ДДУ Шымкент

## 📋 Общая информация

- **Документ**: ДДУ Шымкент (Договор Долевого Участия)
- **Переменных**: 38
- **Дата создания**: 2025-11-03
- **Языки**: Русский, Казахский

## 📊 Структура переменных

### 1. Договор (4 переменных)
- `CONTRACT_NUMBER` - Номер договора
- `CONTRACT_DATE` - Дата договора
- `CONTRACT_PLACE` - Место заключения
- `CONTRACT_YEAR` - Год договора

### 2. Уполномоченная компания (10 переменных)
- `COMPANY_NAME` - Наименование
- `COMPANY_DIRECTOR` - ФИО руководителя
- `COMPANY_BASIS` - Основание полномочий
- `COMPANY_BIN` - БИН
- `COMPANY_ADDRESS` - Адрес
- `COMPANY_PHONE` - Телефон
- `COMPANY_EMAIL` - Email
- `COMPANY_BANK` - Банк
- `COMPANY_ACCOUNT` - Расчетный счет
- `COMPANY_BIK` - БИК банка

### 3. Дольщик (8 переменных)
- `CLIENT_FIO` - ФИО
- `CLIENT_IIN` - ИИН
- `CLIENT_ADDRESS` - Адрес
- `CLIENT_PHONE` - Телефон
- `CLIENT_EMAIL` - Email
- `CLIENT_PASSPORT` - Номер документа
- `CLIENT_PASSPORT_ISSUED_BY` - Кем выдан
- `CLIENT_PASSPORT_DATE` - Дата выдачи

### 4. Объект (6 переменных)
- `APARTMENT_NUMBER` - Номер квартиры
- `APARTMENT_FLOOR` - Этаж
- `APARTMENT_AREA` - Площадь
- `APARTMENT_ROOMS` - Количество комнат
- `BUILDING_ADDRESS` - Адрес дома
- `BUILDING_CADASTRAL` - Кадастровый номер

### 5. Финансы (3 переменных)
- `PRICE_TOTAL` - Стоимость доли
- `PRICE_PER_METER` - Цена за кв.м
- `PAYMENT_SCHEDULE` - График платежей

### 6. Сроки (1 переменная)
- `COMPLETION_DATE` - Срок сдачи

### 7. Документы (4 переменных)
- `ACCEPTANCE_ACT_NUMBER` - Номер акта приемки
- `ACCEPTANCE_ACT_DATE` - Дата акта
- `REGISTRATION_NUMBER` - Номер регистрации
- `REGISTRATION_DATE` - Дата регистрации

### 8. Дополнительно (2 переменных)
- `KEYS_COUNT` - Количество ключей
- `WITNESS_NAME` - ФИО свидетеля

## 📁 Файлы

### 1. `ddu_variables.json`
Полная база данных переменных в формате JSON. Готова для импорта в API.

**Формат:**
```json
{
  "document_id": "uuid",
  "document_name": "ДДУ Шымкент",
  "variables": [
    {
      "id": "uuid",
      "name": "CONTRACT_NUMBER",
      "display_name": "Номер договора",
      "display_name_kz": "Шарт нөмірі",
      "table": "contracts",
      "field": "contract_number",
      "data_type": "string",
      "required": true,
      "example": "ADL-1-204/41"
    }
  ]
}
```

### 2. `ddu_variables.sql`
SQL скрипт для создания таблиц и вставки переменных в базу данных.

**Таблицы:**
- `documents` - Документы
- `document_variables` - Переменные документов

**Использование:**
```bash
mysql -u username -p database_name < ddu_variables.sql
# или
psql -U username -d database_name -f ddu_variables.sql
```

### 3. `ddu_mapping_template.csv`
Excel-таблица для проверки и редактирования маппинга переменных.

**Столбцы:**
- ID
- Имя переменной
- Отображаемое имя (РУ)
- Отображаемое имя (КЗ)
- Категория
- Таблица БД
- Поле БД
- Тип данных
- Обязательное
- Пример значения

**Использование:**
1. Откройте в Excel/Google Sheets
2. Проверьте соответствие таблиц и полей вашей БД
3. Отредактируйте при необходимости
4. Используйте для импорта данных

### 4. `ddu_api_endpoint_example.py`
Пример FastAPI endpoint для работы с переменными ДДУ.

**Endpoints:**
- `GET /ddu/variables` - Получить все переменные
- `POST /ddu/fill` - Заполнить документ данными

## 🚀 Как использовать

### Шаг 1: Импорт в базу данных

```bash
# MySQL
mysql -u root -p printable_forms < ddu_variables.sql

# PostgreSQL
psql -U postgres -d printable_forms -f ddu_variables.sql
```

### Шаг 2: Интеграция в Python backend

```python
# Добавьте в app/api/routes/ddu.py
from pathlib import Path
import json

# Загрузите переменные
with open('variables_export/ddu_variables.json') as f:
    DDU_CONFIG = json.load(f)

@router.get("/ddu/variables")
async def get_ddu_variables():
    return DDU_CONFIG

@router.post("/ddu/fill/{contract_id}")
async def fill_ddu(contract_id: str):
    # Получить данные из БД
    contract = db.query(Contract).filter_by(id=contract_id).first()
    client = contract.client
    apartment = contract.apartment
    
    # Заполнить переменные
    filled = {}
    for var in DDU_CONFIG['variables']:
        table = var['table']
        field = var['field']
        
        # Маппинг на объекты
        if table == 'contracts':
            value = getattr(contract, field)
        elif table == 'clients':
            value = getattr(client, field)
        elif table == 'apartments':
            value = getattr(apartment, field)
        
        filled[var['id']] = str(value)
    
    return {"variables": filled}
```

### Шаг 3: Использование в Word Add-in

```javascript
// В frontend/commands.html

async function fillDDUDocument(event) {
    try {
        // Получаем contract_id
        const contractId = localStorage.getItem('current_contract_id');
        
        // Получаем заполненные переменные из API
        const response = await fetch(
            `${API_BASE_URL}/api/ddu/fill/${contractId}`,
            { headers: { 'X-Session-ID': sessionId } }
        );
        const data = await response.json();
        
        // Заполняем в Word документе
        await Word.run(async (context) => {
            const doc = context.document;
            
            // Для каждой переменной
            for (const [varId, value] of Object.entries(data.variables)) {
                // Найти и заменить плейсхолдер
                const searchResults = doc.body.search(`{${varId}}`, {
                    matchCase: false,
                    matchWholeWord: true
                });
                
                searchResults.load('items');
                await context.sync();
                
                // Заменить на значение
                for (let i = 0; i < searchResults.items.length; i++) {
                    searchResults.items[i].insertText(value, 'Replace');
                }
            }
            
            await context.sync();
        });
        
        event.completed();
    } catch (error) {
        console.error('Error filling document:', error);
        event.completed();
    }
}
```

## 🔧 Настройка шаблона Word

Для того чтобы переменные работали, в Word документе нужно заменить пустые места `___` на плейсхолдеры:

**Было:**
```
Договор № ___ от ___ года
```

**Стало:**
```
Договор № {237701d3-4b58-4c45-ba2d-d0cbe407089b} от {40484073-6912-4517-a596-8bd4359bd7b3} года
```

**Или с читаемыми именами:**
```
Договор № {CONTRACT_NUMBER} от {CONTRACT_DATE} года
```

### Автоматическая замена в Word:

1. Откройте документ ДДУ Шымкент.docx
2. Используйте Find & Replace (Ctrl+H)
3. Замените:
   - Первое `___` (после "Договор №") → `{CONTRACT_NUMBER}`
   - Дату `___` → `{CONTRACT_DATE}`
   - И т.д. для всех переменных

## 📝 Примеры значений

| Переменная | Пример |
|------------|--------|
| CONTRACT_NUMBER | ADL-1-204/41 |
| CONTRACT_DATE | 25.02.2020 |
| CONTRACT_PLACE | г. Нур-Султан |
| COMPANY_NAME | ТОО "Town House" |
| CLIENT_FIO | Петров Петр Петрович |
| CLIENT_IIN | 900101300123 |
| APARTMENT_NUMBER | 204 |
| APARTMENT_FLOOR | 5 |
| APARTMENT_AREA | 65.5 |
| PRICE_TOTAL | 15000000 |
| PRICE_PER_METER | 228000 |

## ❓ FAQ

### Q: Как добавить новую переменную?

A: Отредактируйте `create_ddu_variables.py`, добавьте в список `variables`, запустите скрипт заново.

### Q: Можно ли изменить имена переменных?

A: Да, измените `name` в JSON файле. UUID менять не нужно.

### Q: Как связать с реальной базой данных?

A: Заполните поля `table` и `field` в соответствии с вашей схемой БД.

### Q: Поддерживаются ли вложенные объекты?

A: Да, используйте точечную нотацию: `client.address.city`

### Q: Как обновить документ после изменения переменных?

A: Загрузите новый JSON в API, старые ID останутся прежними.

## 🔗 Связанные документы

- [Основной README](../../README-NEW.md)
- [Быстрый старт](../../QUICKSTART.md)
- [Миграция с C#](../../MIGRATION.md)
- [Создание шаблонов](../HOW_TO_CREATE_TEMPLATE.md)

## 📧 Поддержка

По вопросам: support@example.com

