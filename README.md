# Printable Forms Word Add-in

Word надстройка для работы с печатными формами на Python + JavaScript.

## 🚀 ЗАПУСК

### Способ 1: Автоматический (одна команда)

**Требуется**: Docker Desktop + Node.js

```bash
cd /Users/onyoka/Downloads/word-add-in
./start-all.sh
```

### Способ 2: Вручную (4 команды)

**Требуется**: Docker Desktop + Node.js

```bash
cd /Users/onyoka/Downloads/word-add-in

# 1. Запустить Backend + PostgreSQL
docker-compose up -d

# 2. Перейти в frontend
cd frontend

# 3. Установить зависимости (только первый раз)
npm install

# 4. Запустить
npm run serve
```

📖 [Подробная пошаговая инструкция](РУЧНОЙ_ЗАПУСК.md)

### Вручную (без скриптов):

**1. Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Настройте .env!
python run.py
```

**2. Frontend (новый терминал):**
```bash
cd frontend
npm install
npx office-addin-dev-certs install
npm run serve
```

**3. Установка в Word:**

📖 [Подробная инструкция установки в Word](УСТАНОВКА_В_WORD.md)

**Быстрый способ:**
- Используйте **Word Online** (office.com)
- Или команду: `office-addin-debugging start manifest.xml desktop`

## 📖 Документация

### Запуск:
- 🖐️ [**Ручной запуск (Mac/Linux)**](РУЧНОЙ_ЗАПУСК.md) ⬅️ **Mac пользователи**
- 🪟 [**Запуск на Windows**](WINDOWS_ЗАПУСК.md) ⬅️ **Windows пользователи**
- 🐳 [Docker запуск](DOCKER_ЗАПУСК.md)

### Установка в Word:
- 📄 [**Установка в Word (общая)**](УСТАНОВКА_В_WORD.md)
- 🪟 [**Установка в Word на Windows**](WINDOWS_УСТАНОВКА_НАДСТРОЙКИ.md) ⬅️ **Windows Desktop Word**
- 📝 [ВАЖНО для Windows](ВАЖНО_WINDOWS.txt)

### Функционал:
- 📊 [Сравнение источников данных](backend/DATA_SOURCE_COMPARISON.md)
- ✅ [Что готово в проекте](ЧТО_ГОТОВО.md)

## 🏗️ Архитектура

- **Backend**: Python FastAPI (порт 8000)
- **Frontend**: Office JavaScript Add-in (порт 3000)
- **База данных**: PostgreSQL

## ✨ Возможности

- 📥 **Загрузка шаблонов** - из Printable Forms API (один раз)
- 🤖 **Автоматическое извлечение параметров** - из загруженного документа
- 💾 **Управление параметрами БД** - CRUD интерфейс
- 📝 **Автозаполнение документов** - данные из БД (без API!)
- 🔍 **Поиск параметров** - по договорам и значениям
- ⚡ **Offline режим** - работает без интернета после загрузки шаблона

## 🛠️ Требования

### С Docker (минимальные требования):
- Docker Desktop
- Node.js 18+
- Microsoft Word

### Без Docker:
- Python 3.11+
- Node.js 18+
- PostgreSQL (или MySQL)
- Microsoft Word

## 📞 Поддержка

Вопросы? Читайте [ЗАПУСК.md](ЗАПУСК.md) или создайте issue.

---

**Версия**: 1.0.0  
**Дата**: 2025-11-03
