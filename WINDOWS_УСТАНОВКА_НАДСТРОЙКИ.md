# 🪟 Установка надстройки в Word на Windows

## Проблема: Надстройка не видна в Desktop Word

Это нормально! Для **разработческих надстроек** нужна специальная настройка.

---

## ✅ РЕШЕНИЕ 1: Word Online (РАБОТАЕТ 100%!)

**Самый надежный способ - используйте Word в браузере:**

1. Откройте https://office.com
2. Войдите в ваш Microsoft аккаунт
3. Нажмите **Word** → **Новый пустой документ**
4. **Вставка** → **Надстройки Office**
5. Нажмите **"Отправить мою надстройку"** (внизу окна)
6. Нажмите **"Обзор..."**
7. Выберите файл:
   ```
   C:\Users\ВашеИмя\Downloads\word-add-in\frontend\manifest.xml
   ```
8. Нажмите **"Отправить"**

✅ **Готово!** На ленте Word появятся кнопки **"Печатные формы"**!

**Преимущества Word Online:**
- ✅ Работает сразу, без настроек
- ✅ Не нужны права администратора
- ✅ Легко переустановить
- ✅ Всегда актуальная версия Word

---

## ✅ РЕШЕНИЕ 2: Автоматическая установка (Desktop Word)

Используйте инструмент `office-addin-debugging`:

### Шаг 1: Установите инструмент

Откройте **PowerShell** (НЕ от администратора):

```powershell
npm install -g office-addin-debugging office-addin-dev-certs
```

### Шаг 2: Перейдите в папку frontend

```powershell
cd C:\Users\ВашеИмя\Downloads\word-add-in\frontend
```

### Шаг 3: Запустите

```powershell
office-addin-debugging start manifest.xml desktop
```

✅ **Word откроется автоматически** с установленной надстройкой!

### Чтобы остановить:
```powershell
office-addin-debugging stop manifest.xml
```

---

## ✅ РЕШЕНИЕ 3: Через сетевую папку (для постоянной установки)

Этот способ сложнее, но надстройка будет видна всегда.

### Шаг 1: Создайте папку для надстроек

Откройте **PowerShell**:

```powershell
# Создать папку
$wefPath = "$env:LOCALAPPDATA\Microsoft\Office\16.0\Wef"
New-Item -ItemType Directory -Force -Path $wefPath

# Скопировать манифест
Copy-Item "C:\Users\ВашеИмя\Downloads\word-add-in\frontend\manifest.xml" $wefPath
```

### Шаг 2: Настройте сетевую папку

**PowerShell от администратора:**

```powershell
# Создать сетевую папку
$shareName = "OfficeAddins"
New-SmbShare -Name $shareName -Path $wefPath -FullAccess Everyone
```

Или создайте вручную:
1. Откройте папку: `%LOCALAPPDATA%\Microsoft\Office\16.0\Wef`
2. Правой кнопкой → **Свойства** → **Доступ** → **Общий доступ**
3. Добавьте себя с правами "Чтение"
4. Нажмите **Поделиться**

### Шаг 3: Добавьте в Trust Center Word

1. Откройте **Word**
2. **Файл** → **Параметры**
3. **Центр управления безопасностью** → **Параметры центра управления безопасностью...**
4. **Надежные каталоги надстроек**
5. В поле "URL каталога" вставьте:
   ```
   \\localhost\OfficeAddins
   ```
   Или:
   ```
   file:///C:/Users/ВашеИмя/AppData/Local/Microsoft/Office/16.0/Wef
   ```
6. Нажмите **"Добавить каталог"**
7. Поставьте галочку **"Показывать в меню"**
8. Нажмите **ОК** → **ОК**

### Шаг 4: Перезапустите Word

Закройте Word полностью (Alt+F4) и откройте заново.

### Шаг 5: Найдите надстройку

1. **Вставка** → **Надстройки**
2. **Мои надстройки** → Вкладка **"ОБЩАЯ ПАПКА"**
3. Ваша надстройка должна быть в списке!

---

## ✅ РЕШЕНИЕ 4: Через реестр Windows (продвинутый)

**Только если другие способы не работают!**

### Шаг 1: Создайте файл реестра

Создайте файл `add-addin.reg` с содержимым:

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\WEF\Developer]
"UseDevCatalog"=dword:00000001
"DeveloperCatalogUrl"="file:///C:/Users/ВашеИмя/AppData/Local/Microsoft/Office/16.0/Wef"
```

**ВАЖНО:** Замените `ВашеИмя` на ваше имя пользователя Windows!

### Шаг 2: Выполните файл

Двойной клик на `add-addin.reg` → **Да** → **ОК**

### Шаг 3: Скопируйте манифест

```powershell
Copy-Item "C:\Users\ВашеИмя\Downloads\word-add-in\frontend\manifest.xml" `
          "$env:LOCALAPPDATA\Microsoft\Office\16.0\Wef\"
```

### Шаг 4: Перезапустите Word

---

## 🎯 Рекомендации для Windows:

| Способ | Сложность | Надежность |
|--------|-----------|------------|
| **Word Online** | ⭐ Легко | ✅✅✅ 100% |
| **office-addin-debugging** | ⭐⭐ Средне | ✅✅ 90% |
| **Сетевая папка** | ⭐⭐⭐ Сложно | ✅ 70% |
| **Реестр** | ⭐⭐⭐⭐ Очень сложно | ✅ 80% |

**Рекомендация:** Используйте **Word Online** или **office-addin-debugging**!

---

## 🧪 Проверка установки

После установки:

### 1. Проверьте в Word

На вкладке **"Главная"** должна появиться группа **"Печатные формы"** с кнопками:
- 💾 Параметры БД
- 📄 Выбрать шаблон
- 📝 Заполнить данные

### 2. Нажмите "Параметры БД"

Справа должна открыться панель с таблицей параметров.

### 3. Если не видно кнопок

Откройте **Developer Tools** в Word:
- Нажмите **F12** или **Ctrl+Shift+I**
- Перейдите на вкладку **Console**
- Посмотрите ошибки

---

## ❓ Решение проблем (Windows)

### Проблема: "office-addin-debugging не работает"

**Решение:**

1. Убедитесь что npm установлен глобально:
```powershell
npm config get prefix
```

2. Проверьте PATH:
```powershell
$env:PATH -split ';' | Select-String "npm"
```

3. Переустановите:
```powershell
npm uninstall -g office-addin-debugging
npm cache clean --force
npm install -g office-addin-debugging
```

### Проблема: "Access Denied" при создании сетевой папки

**Решение:**
Запустите PowerShell **от имени администратора**:
1. Правой кнопкой на PowerShell
2. **"Запустить от имени администратора"**

### Проблема: Надстройка загружается но не работает

**Решение:**

1. Проверьте что Frontend запущен:
```powershell
# Откройте браузер
start https://localhost:3000
```

2. Проверьте что Backend работает:
```powershell
start http://localhost:8000/docs
```

3. Проверьте сертификаты:
```powershell
npx office-addin-dev-certs verify
```

Если не работают:
```powershell
npx office-addin-dev-certs install --force
```

### Проблема: "Manifest validation failed"

**Решение:**
```powershell
cd frontend
npm run validate
```

Исправьте ошибки в `manifest.xml` если есть.

---

## 🔧 Очистка кеша Word (Windows)

Если надстройка странно себя ведет:

```powershell
# Остановите Word полностью

# Очистите кеш
Remove-Item "$env:LOCALAPPDATA\Microsoft\Office\16.0\Wef\*" -Recurse -Force

# Перезапустите Word
```

---

## 💻 Альтернатива: Visual Studio Code

Если у вас установлен VS Code:

1. Установите расширение **"Office Add-in Debugger"**
2. Откройте папку проекта в VS Code
3. Нажмите **F5**
4. Выберите **"Word Desktop"**

Word откроется с надстройкой автоматически!

---

## 🎯 ИТОГО: Что делать на Windows?

### Для быстрого теста:
```
Используйте Word Online (office.com)
```

### Для разработки:
```powershell
cd C:\Users\ВашеИмя\Downloads\word-add-in\frontend
npm install -g office-addin-debugging
office-addin-debugging start manifest.xml desktop
```

### Для постоянной работы:
Настройте сетевую папку (Решение 3)

---

## 📞 Если ничего не помогло

### План Б: Создайте bat файл

Создайте файл `install-to-word.bat`:

```batch
@echo off
echo Установка надстройки в Word...

REM Создать папку
mkdir "%LOCALAPPDATA%\Microsoft\Office\16.0\Wef" 2>nul

REM Скопировать манифест
copy /Y "%~dp0frontend\manifest.xml" "%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\"

echo Манифест скопирован!
echo.
echo Теперь:
echo 1. Откройте Word
echo 2. Файл - Параметры - Центр управления безопасностью
echo 3. Параметры центра - Надежные каталоги надстроек
echo 4. Добавьте: %LOCALAPPDATA%\Microsoft\Office\16.0\Wef
echo 5. Поставьте галочку "Показывать в меню"
echo 6. Перезапустите Word
echo.
pause
```

Двойной клик на файл и следуйте инструкциям.

---

**Рекомендация: используйте Word Online - это точно работает на Windows!** 🎉

