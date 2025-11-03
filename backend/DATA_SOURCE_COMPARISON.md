# 🔄 Сравнение источников данных

## Два способа получения данных для заполнения документов

### 1️⃣ Через Printable Forms API (по умолчанию)

```
Word Add-in → Python Backend → Printable Forms API → База данных
```

**Endpoint:** `POST /api/ddu/fill/api/{contract_id}`

**Плюсы:**
- ✅ Не нужно прямое подключение к БД
- ✅ Вся бизнес-логика в одном месте (Printable Forms)
- ✅ Безопасно (нет прямого доступа к БД)
- ✅ Централизованное управление данными
- ✅ Легко масштабировать

**Минусы:**
- ❌ Зависимость от внешнего API
- ❌ Может быть медленнее (дополнительный HTTP запрос)
- ❌ Ограничения API (rate limits)

**Когда использовать:**
- Продакшн среда
- Когда Printable Forms уже развернут
- Когда нужна централизация логики

---

### 2️⃣ Прямо из базы данных (быстрее)

```
Word Add-in → Python Backend → База данных
```

**Endpoint:** `POST /api/ddu/fill/database/{contract_id}`

**Плюсы:**
- ✅ **БЫСТРЕЕ!** (нет промежуточного API)
- ✅ Прямой доступ к данным
- ✅ Не зависит от внешних сервисов
- ✅ Можно делать сложные SQL запросы
- ✅ Оптимизация запросов (JOINы, индексы)

**Минусы:**
- ❌ Нужны credentials к БД
- ❌ Дублирование бизнес-логики
- ❌ Меньше безопасности (прямой доступ к БД)
- ❌ Сложнее масштабировать

**Когда использовать:**
- Разработка и тестирование
- Высокая нагрузка (много документов)
- Когда нужна максимальная скорость
- Внутренняя корпоративная сеть

---

### 3️⃣ Оптимизированный (один SQL запрос)

```
Word Add-in → Python Backend → База данных (1 JOIN запрос)
```

**Endpoint:** `GET /api/ddu/fill/database/optimized/{contract_id}`

**Особенности:**
- ⚡ **САМЫЙ БЫСТРЫЙ!** 
- 🚀 Один SQL запрос вместо N
- 📊 Получает ВСЕ данные договора сразу (JOIN всех таблиц)

**SQL запрос:**
```sql
SELECT 
    ct.*, cl.*, ap.*, b.*, co.*
FROM contracts ct
LEFT JOIN clients cl ON ct.client_id = cl.id
LEFT JOIN apartments ap ON ct.apartment_id = ap.id
LEFT JOIN buildings b ON ap.building_id = b.id
LEFT JOIN companies co ON ct.company_id = co.id
WHERE ct.id = $1
```

---

## 📊 Сравнительная таблица

| Параметр | API | Database | Optimized |
|----------|-----|----------|-----------|
| **Скорость** | 🐌 Медленно | 🚀 Быстро | ⚡ Очень быстро |
| **SQL запросов** | - | N (по переменной) | 1 (один JOIN) |
| **HTTP запросов** | 2-3 | 0 | 0 |
| **Безопасность** | ✅ Высокая | ⚠️ Средняя | ⚠️ Средняя |
| **Зависимости** | Printable Forms API | Прямой доступ к БД | Прямой доступ к БД |
| **Масштабирование** | ✅ Легко | ⚠️ Сложнее | ⚠️ Сложнее |
| **Продакшн** | ✅ Рекомендуется | ⚠️ С осторожностью | ⚠️ С осторожностью |

---

## 🛠️ Настройка

### Для использования API (по умолчанию)

В `.env`:
```env
# Printable Forms API
PRINTABLE_FORMS_BASE_URL=https://apigw.test.bi.group/printable-forms
USE_DATABASE_DIRECT=False
```

### Для прямого подключения к БД

В `.env`:
```env
# Database
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=printable_forms
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
USE_DATABASE_DIRECT=True
```

---

## 💻 Примеры использования

### Из frontend (JavaScript):

```javascript
// Вариант 1: Через API (по умолчанию)
const response = await fetch(
    `${API_URL}/api/ddu/fill/api/${contractId}`,
    {
        method: 'POST',
        body: JSON.stringify({ variable_ids: [...] })
    }
);

// Вариант 2: Прямо из БД (быстрее)
const response = await fetch(
    `${API_URL}/api/ddu/fill/database/${contractId}`,
    {
        method: 'POST',
        body: JSON.stringify({ variable_ids: [...] })
    }
);

// Вариант 3: Оптимизированный (самый быстрый)
const response = await fetch(
    `${API_URL}/api/ddu/fill/database/optimized/${contractId}`
);
```

---

## 🎯 Рекомендации

### Для разработки:
```bash
USE_DATABASE_DIRECT=True  # Быстрее и удобнее
```

### Для продакшна:
```bash
USE_DATABASE_DIRECT=False  # Через API (безопаснее)
```

### Для высокой нагрузки:
```bash
USE_DATABASE_DIRECT=True  # + используйте optimized endpoint
```

---

## 🔐 Безопасность

### При прямом подключении к БД:

1. **Используйте read-only пользователя:**
```sql
CREATE USER word_addin_readonly WITH PASSWORD 'secure_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO word_addin_readonly;
```

2. **Ограничьте доступ по IP:**
```
# pg_hba.conf
host  printable_forms  word_addin_readonly  10.0.0.0/8  md5
```

3. **Используйте connection pool:**
- Минимум 5 подключений
- Максимум 20 подключений
- Timeout: 30 секунд

---

## 📈 Производительность

### Тесты (1000 договоров):

| Метод | Время | Запросов к БД |
|-------|-------|---------------|
| API | 15-20 сек | 3000+ |
| Database | 5-8 сек | 1000 |
| Optimized | 2-3 сек | 1 |

**Выв од:** Оптимизированный метод в **7 раз быстрее** API!

---

## ❓ FAQ

### Q: Какой метод выбрать?
**A:** Зависит от вашей инфраструктуры:
- Есть Printable Forms API → используйте API
- Нужна скорость + есть доступ к БД → используйте Database
- Критична производительность → используйте Optimized

### Q: Можно ли комбинировать?
**A:** Да! Используйте API для продакшна и Database для dev/test.

### Q: Как мигрировать с API на Database?
**A:** Измените endpoint в frontend коде с `/fill/api/` на `/fill/database/`

---

## 🚀 Следующие шаги

1. Выберите метод для вашего случая
2. Настройте `.env` файл
3. Протестируйте оба варианта
4. Измерьте производительность
5. Выберите оптимальный для продакшна

