# 🪟 Запуск на Windows

## Что нужно установить:

### 1. Docker Desktop для Windows
**Скачать**: https://www.docker.com/products/docker-desktop

После установки:
- Запустите Docker Desktop
- Подождите пока иконка станет зеленой
- Убедитесь что WSL2 включен (Docker сам предложит)

### 2. Node.js
**Скачать**: https://nodejs.org/

Выберите LTS версию (18 или выше).

---

## 🚀 Запуск (PowerShell или CMD)

### ТЕРМИНАЛ 1 - Backend + PostgreSQL

Откройте **PowerShell** или **CMD** и выполните:

```powershell
# 1. Перейти в папку проекта
cd C:\Users\ВашеИмя\Downloads\word-add-in

# Или где у вас лежит проект:
cd путь\к\word-add-in

# 2. Запустить Docker контейнеры
docker-compose up -d

# 3. Подождать 15-20 секунд
timeout /t 15

# 4. Проверить что работает
curl http://localhost:8000/health
```

Если `curl` не работает, откройте в браузере:
```
http://localhost:8000/docs
```

Должен открыться Swagger UI.

✅ **Backend готов!**

---

### ТЕРМИНАЛ 2 - Frontend

Откройте **НОВЫЙ PowerShell** или **CMD**:

```powershell
# 1. Перейти в папку frontend
cd C:\Users\ВашеИмя\Downloads\word-add-in\frontend

# 2. Установить зависимости (ТОЛЬКО ПЕРВЫЙ РАЗ!)
npm install

# 3. Установить SSL сертификаты (ТОЛЬКО ПЕРВЫЙ РАЗ!)
npx office-addin-dev-certs install

# 4. Запустить dev сервер
npm run serve
```

Должны увидеть:
```
Server running at https://localhost:3000
```

✅ **Frontend готов!**

---

## 📄 Установка в Word (Windows)

### Способ 1: Word Online (ПРОЩЕ ВСЕГО!)

1. Откройте https://office.com в браузере
2. Войдите в Microsoft аккаунт
3. Откройте **Word Online** → Создать новый документ
4. **Вставка** → **Надстройки Office**
5. Нажмите **"Отправить мою надстройку"** (внизу справа)
6. Выберите файл `manifest.xml` из папки:
   ```
   C:\Users\ВашеИмя\Downloads\word-add-in\frontend\manifest.xml
   ```
7. Нажмите **"Отправить"**

✅ **Надстройка установлена!** Кнопки появятся на ленте!

---

### Способ 2: Автоматическая установка

В **PowerShell**:

```powershell
cd C:\Users\ВашеИмя\Downloads\word-add-in\frontend

# Установить инструмент (только первый раз)
npm install -g office-addin-debugging

# Запустить (Word откроется автоматически!)
office-addin-debugging start manifest.xml desktop
```

Word откроется с уже установленной надстройкой!

---

### Способ 3: Через сетевую папку (для Desktop Word)

**Шаг 1:** Создайте папку для надстроек:

```powershell
mkdir %LOCALAPPDATA%\Microsoft\Office\16.0\Wef
```

**Шаг 2:** Скопируйте манифест:

```powershell
copy "C:\Users\ВашеИмя\Downloads\word-add-in\frontend\manifest.xml" ^
     "%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\"
```

**Шаг 3:** Настройте Trust Center в Word:

1. Откройте **Word**
2. **Файл** → **Параметры** → **Центр управления безопасностью**
3. **Параметры центра управления безопасностью...**
4. **Надежные каталоги надстроек**
5. В поле "URL каталога" введите:
   ```
   C:\Users\ВашеИмя\AppData\Local\Microsoft\Office\16.0\Wef
   ```
6. Нажмите **"Добавить каталог"**
7. Поставьте галочку **"Показывать в меню"**
8. Нажмите **"ОК"** → **"ОК"**

**Шаг 4:** Перезапустите Word

**Шаг 5:** **Вставка** → **Мои надстройки** → **ОБЩАЯ ПАПКА**

Там будет ваша надстройка!

---

## 🧪 Проверка

После установки:

### 1. Проверьте что Backend работает

Откройте браузер: http://localhost:8000/docs

Должен открыться Swagger UI с API документацией.

### 2. Проверьте Frontend

Откройте: https://localhost:3000/test-cors.html

Нажмите кнопки для проверки подключения.

### 3. Проверьте в Word

Нажмите кнопку **"Параметры БД"** в Word.

Должна открыться панель справа с таблицей параметров.

---

## 🛑 Остановка

### Остановить Frontend:
Нажмите **Ctrl+C** в окне PowerShell с npm

### Остановить Backend:
```powershell
docker-compose down
```

---

## 📝 Команды для копирования (Windows)

### Backend (Docker):
```powershell
cd C:\Users\ВашеИмя\Downloads\word-add-in
docker-compose up -d
```

### Frontend:
```powershell
cd C:\Users\ВашеИмя\Downloads\word-add-in\frontend
npm install
npx office-addin-dev-certs install
npm run serve
```

### Установка в Word:
```powershell
cd frontend
npm install -g office-addin-debugging
office-addin-debugging start manifest.xml desktop
```

---

## ❓ Решение проблем (Windows)

### Проблема: "docker-compose не является командой"

**Решение:**
1. Убедитесь что Docker Desktop установлен и запущен
2. Перезапустите PowerShell
3. Попробуйте:
```powershell
docker compose up -d
```
(без дефиса, новая версия Docker)

### Проблема: "npm не является командой"

**Решение:**
1. Установите Node.js: https://nodejs.org/
2. Перезапустите PowerShell
3. Проверьте:
```powershell
node --version
npm --version
```

### Проблема: PowerShell блокирует выполнение скриптов

**Решение:**
Запустите PowerShell **от имени администратора**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Проблема: "Port 8000 already in use"

**Решение:**
```powershell
# Найти процесс
netstat -ano | findstr :8000

# Убить процесс (замените PID на номер из предыдущей команды)
taskkill /PID номер_процесса /F
```

### Проблема: Word не находит надстройку

**Решение:**
Используйте **Word Online** (office.com) - работает всегда!

Или автоматический способ:
```powershell
cd frontend
office-addin-debugging start manifest.xml desktop
```

---

## 🎯 Рекомендации для Windows:

### Для тестирования:
✅ **Word Online** (office.com) - работает 100%

### Для разработки:
✅ **office-addin-debugging** - автоматическая установка

### PowerShell vs CMD:
✅ Используйте **PowerShell** (более современный)

### Docker:
✅ Убедитесь что включен **WSL2** (Docker использует его)

---

## 💡 Специфика Windows:

### 1. Пути к файлам

На Windows пути используют обратный слэш `\`:
```
C:\Users\ВашеИмя\Downloads\word-add-in\frontend\manifest.xml
```

### 2. Переменные окружения

Просмотр:
```powershell
$env:PATH
```

### 3. Разделитель команд

В PowerShell используйте `;`:
```powershell
cd frontend; npm install; npm run serve
```

В CMD используйте `&`:
```cmd
cd frontend & npm install & npm run serve
```

---

## 📦 Пакетный файл для быстрого запуска (Windows)

Создал файл `start-windows.bat` для автоматического запуска.

Просто **двойной клик** на файл!

---

## 🔥 Быстрая команда (всё в одном):

### PowerShell:
```powershell
cd C:\Users\ВашеИмя\Downloads\word-add-in; `
docker-compose up -d; `
Start-Sleep -Seconds 15; `
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run serve"
```

Эта команда:
1. Запустит Docker
2. Подождет 15 секунд
3. Откроет новое окно PowerShell с Frontend

---

## 📞 Поддержка

Проблемы на Windows?
- Читайте документацию Docker Desktop
- Проверьте что WSL2 установлен
- Используйте Word Online для быстрого тестирования

---

**Всё готово для работы на Windows! 🪟**

