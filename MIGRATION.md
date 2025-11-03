# Миграция с C# на Python

Этот документ описывает, как был мигрирован проект с C# VSTO Add-in на Python FastAPI + Office JavaScript Add-in.

## Что было переписано

### ✅ Backend (Python FastAPI)

#### Модели (C# → Python Pydantic)

| C# Class | Python Model | Файл |
|----------|--------------|------|
| `KeyCloakToken` | `KeyCloakToken` | `app/models/keycloak.py` |
| `KeyCloakError` | `KeyCloakError` | `app/models/keycloak.py` |
| `KeyCloakResponse` | `KeyCloakResponse` | `app/models/keycloak.py` |
| `DocumentVariable` | `DocumentVariable` | `app/models/document.py` |
| `PfDocument` | `PfDocument` | `app/models/document.py` |

#### Сервисы

| C# Service | Python Service | Файл |
|------------|----------------|------|
| `KeyCloakService` | `KeyCloakService` | `app/services/keycloak_service.py` |
| `PfApiService` | `PfApiService` | `app/services/pf_api_service.py` |
| `MemoryCacheService` | `CacheService` | `app/services/cache_service.py` |

#### API Endpoints

| Функциональность | C# Presenter | Python Endpoint |
|------------------|--------------|-----------------|
| Логин | `LoginPresenter` | `POST /api/auth/login` |
| Выход | `LoginPresenter` | `POST /api/auth/logout` |
| Список документов | `FilePresenter` | `GET /api/documents/list` |
| Скачать документ | `FilePresenter` | `GET /api/documents/download/{id}` |
| Переменные документа | `PreviewPresenter` | `GET /api/variables/document/{id}` |
| Значения переменных | `PreviewPresenter` | `POST /api/variables/values` |

### ✅ Frontend (Office JavaScript Add-in)

#### UI Компоненты

| C# View | JavaScript HTML | Файл |
|---------|-----------------|------|
| `LoginView` | Login page | `frontend/login.html` |
| `FileView` | Documents selection | `frontend/documents.html` |
| `TaskPaneView` | Main taskpane | `frontend/taskpane.html` |
| `RibbonUI` | Ribbon buttons | Определены в `manifest.xml` |

#### Функциональность

| C# | JavaScript | Файл |
|----|------------|------|
| `ThisAddIn` | Office.onReady() | Каждая HTML страница |
| Ribbon buttons | Manifest commands | `manifest.xml` |
| Document.Variables | Office.js API | `commands.html` |

## Основные изменения

### 1. Архитектура

**Было (C# VSTO):**
- Монолитное приложение
- Запускается локально на клиенте
- COM интеграция с Word
- Только Windows

**Стало (Python + JS):**
- Разделение на Backend/Frontend
- Backend на сервере
- Frontend через Office.js
- Кроссплатформенность (Windows, Mac, Web)

### 2. Аутентификация

**Было:**
```csharp
var token = keyCloakService.ValidateUser(username, password);
MemoryCacheService.CacheToken(token);
```

**Стало:**
```python
# Backend
response = await keycloak_service.validate_user(username, password)
cache_service.cache_token(session_id, response.data)
```

```javascript
// Frontend
const response = await apiService.login(username, password);
localStorage.setItem('pf_session_id', response.session_id);
```

### 3. Работа с документами

**Было (C#):**
```csharp
var doc = Globals.ThisAddIn.Application.Documents.Open(filePath);
doc.Variables[i].Value = value;
doc.Fields.Update();
```

**Стало (JavaScript):**
```javascript
await Word.run(async (context) => {
    const doc = context.document;
    const variables = doc.properties.customProperties;
    variables.items[i].value = value;
    await context.sync();
});
```

### 4. HTTP Запросы

**Было (C#):**
```csharp
using (var client = new HttpClient())
{
    var response = await client.SendAsync(request);
    return JsonConvert.DeserializeObject<T>(await response.Content.ReadAsStringAsync());
}
```

**Стало (Python):**
```python
async with httpx.AsyncClient() as client:
    response = await client.get(url, headers=headers)
    return [Model(**item) for item in response.json()]
```

### 5. Кеширование

**Было (C#):**
```csharp
private IMemoryCache memoryCache = new MemoryCache(new MemoryCacheOptions());
memoryCache.Set("token", token);
```

**Стало (Python):**
```python
from cachetools import TTLCache
self._cache = TTLCache(maxsize=100, ttl=3600)
self._cache[f"token:{session_id}"] = token
```

## Преимущества новой архитектуры

### ✅ Кроссплатформенность
- Работает на Windows, Mac, Word Online
- Одна кодовая база для всех платформ

### ✅ Современный стек
- Python FastAPI - быстрый и современный
- Async/await для производительности
- Pydantic для валидации данных
- Автоматическая документация API (Swagger)

### ✅ Разделение ответственности
- Backend: бизнес-логика на Python
- Frontend: только UI на JavaScript
- Легче тестировать и поддерживать

### ✅ Масштабируемость
- Backend можно масштабировать независимо
- Легко добавить несколько frontend клиентов
- Возможность добавить mobile apps в будущем

### ✅ DevOps
- Docker для развертывания
- CI/CD friendly
- Легко настроить мониторинг

## Что осталось сделать

### 🔲 Тестирование
- [ ] Unit тесты для Python сервисов
- [ ] Integration тесты для API
- [ ] E2E тесты для frontend

### 🔲 Безопасность
- [ ] Rate limiting на API
- [ ] Логирование всех запросов
- [ ] Ротация токенов

### 🔲 UI/UX
- [ ] Иконки для кнопок
- [ ] Анимации загрузки
- [ ] Лучшая обработка ошибок

### 🔲 Производительность
- [ ] Redis для кеша (вместо in-memory)
- [ ] CDN для frontend ассетов
- [ ] Сжатие ответов API

### 🔲 Документация
- [ ] API примеры для разработчиков
- [ ] Видео-туториалы
- [ ] FAQ

## Обратная совместимость

⚠️ **Внимание:** Новая версия НЕ совместима со старой C# версией.

Причины:
1. Другой формат манифеста (XML vs новый XML)
2. Другие URLs endpoints
3. Другая структура данных в API

Если нужна миграция данных из старой версии, свяжитесь с разработчиками.

## Поддержка

Вопросы по миграции:
- Email: dev@example.com
- Issues: GitHub Issues

---

Документ обновлен: 2025-11-03

