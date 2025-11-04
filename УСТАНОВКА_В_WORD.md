# 📄 Установка надстройки в Word (для разработки)

## Проблема: "Мои надстройки" открывает магазин

Да, это нормально! Для **разработческих надстроек** используется другой способ.

---

## ✅ ПРАВИЛЬНЫЙ СПОСОБ (Sideloading)

### Для Mac:

#### Способ 1: Через папку wef (рекомендуется)

**Шаг 1:** Создайте папку для надстроек (если нет):
```bash
mkdir -p ~/Library/Containers/com.microsoft.Word/Data/Documents/wef
```

**Шаг 2:** Скопируйте манифест:
```bash
cp /Users/onyoka/Downloads/word-add-in/frontend/manifest.xml \
   ~/Library/Containers/com.microsoft.Word/Data/Documents/wef/
```

**Шаг 3:** Перезапустите Word

**Шаг 4:** Откройте Word → **Insert** → **Add-ins**

Ваша надстройка должна появиться в списке!

---

#### Способ 2: Через Developer Mode

**Шаг 1:** Включите режим разработчика в Word

1. Откройте Word
2. **Word** → **Preferences** (Настройки)
3. **Security & Privacy** (Безопасность)
4. Установите галочку: **"Enable Add-in Development"**

**Шаг 2:** Перезапустите Word

**Шаг 3:** Теперь в меню появится:
- **Insert** → **Add-ins** → **More Add-ins**
- Внизу окна будет ссылка **"Upload My Add-in"**

---

### Для Windows:

#### Способ 1: Через сетевую папку (Shared Folder)

**Шаг 1:** Создайте сетевую папку:
```powershell
# В PowerShell
mkdir C:\Users\%USERNAME%\AppData\Local\Microsoft\Office\16.0\Wef
```

**Шаг 2:** Скопируйте манифест:
```powershell
copy "C:\Users\...\word-add-in\frontend\manifest.xml" ^
     "C:\Users\%USERNAME%\AppData\Local\Microsoft\Office\16.0\Wef\"
```

**Шаг 3:** Добавьте папку в доверенные каталоги:

1. Откройте **File Explorer**
2. Правой кнопкой на папку `Wef` → **Properties** → **Sharing**
3. Нажмите **Share** → добавьте себя с правами "Read"

**Шаг 4:** Настройте Trust Center:

1. Откройте Word
2. **File** → **Options** → **Trust Center** → **Trust Center Settings**
3. **Trusted Add-in Catalogs**
4. Добавьте путь: `\\localhost\c$\Users\<YOUR_NAME>\AppData\Local\Microsoft\Office\16.0\Wef`
5. Поставьте галочку **"Show in Menu"**

---

#### Способ 2: Office Developer Tools (проще!)

**Шаг 1:** Установите Office Add-in Debugger:
```bash
npm install -g office-addin-debugging
```

**Шаг 2:** Запустите надстройку:
```bash
cd /Users/onyoka/Downloads/word-add-in/frontend
npx office-addin-debugging start manifest.xml desktop
```

Word откроется автоматически с установленной надстройкой!

---

## 🌐 Для Word Online (в браузере)

**Самый простой способ для разработки!**

**Шаг 1:** Откройте Word Online:
- Перейдите на https://office.com
- Войдите в Microsoft аккаунт
- Откройте Word Online

**Шаг 2:** Создайте документ

**Шаг 3:** Загрузите надстройку:
1. **Insert** → **Office Add-ins**
2. Нажмите **"Upload My Add-in"** (внизу)
3. Нажмите **"Browse..."**
4. Выберите `manifest.xml`
5. Нажмите **"Upload"**

✅ **Работает сразу!** Без всяких настроек!

---

## 🔧 Альтернативный способ (для всех платформ)

### Используйте office-addin-debugging

**Шаг 1:** Установите глобально:
```bash
npm install -g office-addin-debugging office-addin-dev-certs
```

**Шаг 2:** Перейдите в папку frontend:
```bash
cd /Users/onyoka/Downloads/word-add-in/frontend
```

**Шаг 3:** Запустите:
```bash
office-addin-debugging start manifest.xml desktop
```

**Word автоматически откроется** с установленной надстройкой!

Для остановки:
```bash
office-addin-debugging stop manifest.xml
```

---

## 🎯 Рекомендации

### Для Mac:
✅ **Используйте Word Online** или **Способ 2 (Developer Mode)**

### Для Windows:
✅ **Используйте office-addin-debugging** (автоматический способ)

### Для всех:
✅ **Word Online** - самый простой, работает сразу!

---

## ❓ Решение проблем

### Проблема: Надстройка не появляется после установки

**Решение:**
1. Закройте Word **полностью** (Cmd+Q на Mac)
2. Очистите кеш:
```bash
# Mac
rm -rf ~/Library/Containers/com.microsoft.Word/Data/Library/Caches/*

# Windows
# Удалите: %LOCALAPPDATA%\Microsoft\Office\16.0\Wef\
```
3. Откройте Word заново
4. Попробуйте другой способ установки

### Проблема: "Manifest validation failed"

**Решение:**
Проверьте манифест:
```bash
cd frontend
npm run validate
```

Если есть ошибки, они будут показаны.

### Проблема: Надстройка появляется но не загружается

**Решение:**
1. Убедитесь что Frontend запущен (https://localhost:3000)
2. Проверьте сертификаты:
```bash
npx office-addin-dev-certs verify
```
3. Откройте Developer Console в Word (Cmd+Option+I на Mac)
4. Посмотрите ошибки в Console

---

## 🧪 Быстрый тест

После установки надстройки:

1. Нажмите **"Параметры БД"** в Word
2. Должна открыться панель справа
3. Должна загрузиться таблица с параметрами

Если что-то не работает:
- Откройте **Developer Tools** в Word (F12 или Cmd+Option+I)
- Посмотрите **Console** на ошибки
- Проверьте что Backend работает: http://localhost:8000/health

---

## 💡 Самый надежный способ для тестирования:

### Word Online (работает 100%):

1. Откройте https://office.com
2. Word Online → Новый документ
3. Insert → Office Add-ins → Upload My Add-in
4. Выберите manifest.xml
5. **Готово!**

**Преимущества:**
- ✅ Не нужна установка на компьютер
- ✅ Работает сразу
- ✅ Легко переустановить
- ✅ Актуальная версия Word

---

## 📞 Если ничего не помогло

Попробуйте автоматический инструмент:

```bash
cd frontend
npm install -g office-addin-debugging
office-addin-debugging start manifest.xml desktop
```

Это должно открыть Word с надстройкой автоматически!

---

**Итого: используйте Word Online или office-addin-debugging!** 🎉

