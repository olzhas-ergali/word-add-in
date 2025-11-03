# Printable Forms Word Add-in

Word надстройка для работы с печатными формами на Python + JavaScript.

## 🚀 ЗАПУСК ОДНОЙ КОМАНДОЙ!

**Требуется**: Docker Desktop + Node.js

```bash
cd /Users/onyoka/Downloads/word-add-in
./start-all.sh
```

✅ **Готово!** Скрипт запустит:
- PostgreSQL в Docker
- Backend в Docker  
- Frontend локально
- Автоматически создаст БД и таблицы
- Установит все зависимости

**Время**: 30-60 сек первый раз, 10-15 сек потом.

📖 [Подробная инструкция](ИНСТРУКЦИЯ.md)

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

**3. Word:**
- Insert → Add-ins → My Add-ins
- Upload My Add-in → выберите `frontend/manifest.xml`

## 📖 Документация

### Запуск:
- 🐳 [**Docker запуск (рекомендуется)**](DOCKER_ЗАПУСК.md) ⬅️ **САМЫЙ ПРОСТОЙ!**
- 📝 [Простой запуск за 3 шага](ПРОСТОЙ_ЗАПУСК.md)
- 🚀 [Полная инструкция](ЗАПУСК.md)
- 🎯 [Быстрый старт](QUICKSTART.md)

### Функционал:
- 🔓 [Настройка без авторизации](NO_AUTH_SETUP.md)
- 📊 [Сравнение источников данных](backend/DATA_SOURCE_COMPARISON.md)
- 📝 [Как создавать шаблоны](HOW_TO_CREATE_TEMPLATE.md)

## 🏗️ Архитектура

- **Backend**: Python FastAPI (порт 8000)
- **Frontend**: Office JavaScript Add-in (порт 3000)
- **База данных**: PostgreSQL

## ✨ Возможности

- 💾 **Управление параметрами БД** - CRUD интерфейс
- 📄 **Выбор шаблонов** - из API или БД
- 📝 **Автозаполнение документов** - переменные из БД
- 🔍 **Поиск параметров** - по договорам и значениям

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
