# Printable Forms Word Add-in

Современная надстройка для Microsoft Word с поддержкой KeyCloak аутентификации и работы с печатными формами.

## 🏗️ Архитектура

Проект построен на гибридной архитектуре:

- **Backend**: Python FastAPI (80% логики)
  - REST API endpoints
  - Интеграция с KeyCloak
  - Работа с Printable Forms API
  - Кеширование токенов

- **Frontend**: Office JavaScript Add-in (20% логики)
  - UI для Word
  - Ribbon кнопки
  - Task Panes
  - Интеграция с Office.js

## 📋 Требования

### Backend
- Python 3.11+
- pip или poetry

### Frontend
- Node.js 18+
- npm или yarn
- Microsoft Word (Desktop, Mac или Web)

### Docker (опционально)
- Docker 20+
- Docker Compose 2+

## 🚀 Быстрый старт

### Способ 1: Docker Compose (рекомендуется)

1. **Клонируйте репозиторий**
```bash
git clone <repository-url>
cd word-add-in
```

2. **Настройте переменные окружения**
```bash
cp .env.example .env
# Отредактируйте .env и добавьте ваши настройки
```

3. **Запустите сервисы**
```bash
docker-compose up -d
```

Backend будет доступен на `http://localhost:8000`

### Способ 2: Ручная установка

#### Backend

1. **Перейдите в директорию backend**
```bash
cd backend
```

2. **Создайте виртуальное окружение**
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

3. **Установите зависимости**
```bash
pip install -r requirements.txt
```

4. **Настройте переменные окружения**
```bash
cp .env.example .env
# Отредактируйте .env
```

5. **Запустите сервер**
```bash
python run.py
```

API будет доступен на `http://localhost:8000`

#### Frontend

1. **Перейдите в директорию frontend**
```bash
cd frontend
```

2. **Установите зависимости**
```bash
npm install
```

3. **Сгенерируйте SSL сертификаты для разработки**
```bash
npx office-addin-dev-certs install
```

4. **Запустите dev сервер**
```bash
npm run serve
```

Frontend будет доступен на `https://localhost:3000`

5. **Загрузите манифест в Word**

**Windows/Mac:**
- Откройте Word
- Перейдите в Insert > Add-ins > My Add-ins
- Выберите "Upload My Add-in"
- Выберите файл `manifest.xml`

**Word Online:**
- Откройте документ в Word Online
- Insert > Office Add-ins > Upload My Add-in
- Выберите файл `manifest.xml`

## 📁 Структура проекта

```
word-add-in/
├── backend/                    # Python FastAPI backend
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/        # API endpoints
│   │   │       ├── auth.py    # Аутентификация
│   │   │       ├── documents.py # Документы
│   │   │       └── variables.py # Переменные
│   │   ├── models/            # Pydantic модели
│   │   │   ├── keycloak.py
│   │   │   ├── document.py
│   │   │   └── requests.py
│   │   ├── services/          # Бизнес-логика
│   │   │   ├── keycloak_service.py
│   │   │   ├── pf_api_service.py
│   │   │   └── cache_service.py
│   │   ├── config.py          # Настройки
│   │   └── main.py            # FastAPI приложение
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py
│
├── frontend/                   # Office JavaScript Add-in
│   ├── src/
│   │   ├── api.js            # API клиент
│   │   ├── config.js         # Конфигурация
│   │   └── styles.css        # Стили
│   ├── login.html            # Страница входа
│   ├── documents.html        # Выбор документов
│   ├── commands.html         # Command handlers
│   ├── taskpane.html         # Основная панель
│   ├── manifest.xml          # Манифест надстройки
│   └── package.json
│
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🔧 Конфигурация

### Backend (.env)

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# CORS Settings
CORS_ORIGINS=["https://localhost:3000"]

# Printable Forms API
PRINTABLE_FORMS_BASE_URL=https://apigw.test.bi.group/printable-forms
PRINTABLE_FORMS_GET_FILE_LIST_API=/api/v1/Document/ListMetadata
PRINTABLE_FORMS_GET_DOCX_API=/api/v1/Document/GetDocx
PRINTABLE_FORMS_GET_DOC_VARIABLES_API=/api/v1/DocumentVariable/ListByDocumentId
PRINTABLE_FORMS_GET_VARIABLE_VALUES_API=/api/v1/DocumentVariable/GetVariableValues

# KeyCloak Configuration
KEYCLOAK_CLIENT_API=https://sso.test.bi.group/realms/bi-group/protocol/openid-connect/token
KEYCLOAK_CLIENT_ID=printable-forms
KEYCLOAK_CLIENT_SECRET=your_secret_here

# Cache Settings
CACHE_TTL=3600
```

### Frontend (src/config.js)

```javascript
const CONFIG = {
    API_BASE_URL: 'http://localhost:8000',
    // ... другие настройки
};
```

## 📖 API Документация

После запуска backend, документация доступна по адресам:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Основные endpoints:

#### Аутентификация
- `POST /api/auth/login` - Вход в систему
- `POST /api/auth/logout` - Выход
- `GET /api/auth/validate` - Проверка сессии

#### Документы
- `GET /api/documents/list` - Список шаблонов
- `GET /api/documents/download/{id}` - Скачать документ
- `GET /api/documents/{id}/metadata` - Метаданные документа

#### Переменные
- `GET /api/variables/document/{id}` - Переменные документа
- `POST /api/variables/values` - Значения переменных

## 💡 Использование

### 1. Вход в систему

1. Откройте Word
2. На вкладке "Главная" найдите группу "Печатные формы"
3. Нажмите кнопку "Войти"
4. Введите логин и пароль KeyCloak
5. Нажмите "Войти"

### 2. Выбор шаблона

1. Нажмите кнопку "Выбрать шаблон"
2. Выберите нужный документ из списка
3. Нажмите "Выбрать"
4. Документ откроется в Word

### 3. Заполнение данных

1. Убедитесь, что документ с переменными открыт
2. Нажмите кнопку "Заполнить данные"
3. Переменные будут автоматически заполнены значениями из API

### 4. Выход

1. Нажмите кнопку "Выйти"
2. Сессия будет завершена

## 🧪 Разработка

### Backend

**Запуск в режиме разработки:**
```bash
cd backend
python run.py
# API запустится с hot-reload
```

**Добавление новых зависимостей:**
```bash
pip install <package-name>
pip freeze > requirements.txt
```

### Frontend

**Запуск dev сервера:**
```bash
cd frontend
npm run serve
```

**Валидация манифеста:**
```bash
npm run validate
```

## 🐛 Отладка

### Backend

1. Проверьте логи:
```bash
docker-compose logs backend
```

2. Проверьте health endpoint:
```bash
curl http://localhost:8000/health
```

### Frontend

1. Откройте Developer Tools в Word:
   - Windows: F12
   - Mac: Cmd+Option+I

2. Проверьте Console на ошибки

3. Проверьте localStorage:
```javascript
console.log(localStorage.getItem('pf_session_id'));
```

## 🔒 Безопасность

- Токены хранятся в памяти на backend (TTL кеш)
- Session ID передается через заголовки
- HTTPS обязателен для production
- CORS настроен для разрешенных доменов

## 🚢 Деплой в Production

### Backend

1. **Обновите .env**
```env
API_DEBUG=False
CORS_ORIGINS=["https://your-domain.com"]
```

2. **Используйте production WSGI сервер:**
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

### Frontend

1. **Обновите manifest.xml:**
   - Замените `localhost:3000` на ваш домен
   - Обновите URLs для production

2. **Настройте HTTPS:**
   - Используйте действительный SSL сертификат
   - Настройте reverse proxy (nginx/apache)

3. **Опубликуйте в AppSource (опционально):**
   - Следуйте гайдам Microsoft Office Store

## 📝 Лицензия

MIT

## 🤝 Вклад

Приветствуются Pull Requests!

## 📧 Поддержка

По вопросам обращайтесь: support@example.com

---

**Приятной работы! 🎉**

# word-add-in
