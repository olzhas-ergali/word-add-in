# 🐳 Запуск через Docker (самый простой способ!)

## Зачем Docker?

✅ **Не нужно устанавливать PostgreSQL**  
✅ **Не нужно настраивать Python окружение**  
✅ **Всё работает из коробки**  
✅ **Одна команда для запуска**  

---

## 📋 Что нужно установить:

### 1. Docker Desktop
- **Mac**: [Скачать Docker Desktop для Mac](https://www.docker.com/products/docker-desktop)
- **Windows**: [Скачать Docker Desktop для Windows](https://www.docker.com/products/docker-desktop)

### 2. Node.js (только для Frontend)
- [Скачать Node.js](https://nodejs.org/)

### 3. Microsoft Word
- Любая версия

---

## 🚀 Быстрый запуск

### Способ 1: Автоматический (рекомендую!)

```bash
cd /Users/onyoka/Downloads/word-add-in

# Запустить Backend + БД в Docker
./docker-start.sh

# В другом терминале запустить Frontend
./frontend-start.sh
```

### Способ 2: Вручную

**Терминал 1 - Backend + БД:**
```bash
cd /Users/onyoka/Downloads/word-add-in
docker-compose up -d
```

**Терминал 2 - Frontend:**
```bash
cd /Users/onyoka/Downloads/word-add-in/frontend
npm install
npm run serve
```

---

## 📊 Что запускается в Docker:

```
Docker Compose
├── PostgreSQL (порт 5432)
│   ├── База данных: printable_forms
│   ├── Пользователь: postgres
│   └── Пароль: postgres (или из .env)
│
└── Python Backend (порт 8000)
    ├── FastAPI сервер
    ├── Подключение к PostgreSQL
    └── REST API endpoints
```

**Frontend** запускается ЛОКАЛЬНО (не в Docker) на порту 3000.

---

## ✅ Проверка что всё работает

### 1. Проверьте контейнеры:
```bash
docker-compose ps
```

Должны видеть:
```
NAME            STATUS          PORTS
pf-postgres     Up (healthy)    5432
pf-backend      Up              8000
```

### 2. Проверьте Backend:
```bash
curl http://localhost:8000/health
```

Ответ:
```json
{
  "status": "healthy",
  "api_version": "1.0.0"
}
```

### 3. Проверьте БД:
```bash
docker exec -it pf-postgres psql -U postgres -d printable_forms -c "SELECT COUNT(*) FROM contract_parameters;"
```

Должно показать количество параметров (например: `9`).

### 4. Откройте API документацию:
```
http://localhost:8000/docs
```

---

## 🎯 Установка в Word

### 1. Откройте Word

### 2. Загрузите надстройку:
- **Insert** → **Add-ins** → **My Add-ins**
- **Upload My Add-in**
- Выберите: `/Users/onyoka/Downloads/word-add-in/frontend/manifest.xml`

### 3. Используйте кнопки:
- **Параметры БД** - управление параметрами
- **Выбрать шаблон** - выбор документа
- **Заполнить данные** - автозаполнение

---

## 🔧 Управление контейнерами

### Запуск:
```bash
docker-compose up -d
```

### Остановка:
```bash
docker-compose down
```

### Перезапуск:
```bash
docker-compose restart
```

### Логи Backend:
```bash
docker-compose logs -f backend
```

### Логи PostgreSQL:
```bash
docker-compose logs -f db
```

### Логи всех сервисов:
```bash
docker-compose logs -f
```

### Зайти в контейнер Backend:
```bash
docker exec -it pf-backend /bin/bash
```

### Зайти в PostgreSQL:
```bash
docker exec -it pf-postgres psql -U postgres -d printable_forms
```

---

## 🗄️ Работа с базой данных

### Подключиться к БД:
```bash
docker exec -it pf-postgres psql -U postgres -d printable_forms
```

### Посмотреть параметры:
```sql
SELECT * FROM contract_parameters;
```

### Добавить параметр:
```sql
INSERT INTO contract_parameters (contract_id, param_name, param_value, description)
VALUES ('TEST-001', 'CLIENT_FIO', 'Иванов Иван', 'Тестовый клиент');
```

### Выйти из psql:
```sql
\q
```

---

## 📁 Структура Docker

```
Docker Network: pf-network
│
├── pf-postgres (PostgreSQL 16)
│   ├── Порт: 5432
│   ├── База: printable_forms
│   ├── Volume: postgres_data (сохраняет данные)
│   └── Init SQL: автоматически создает таблицы
│
└── pf-backend (Python FastAPI)
    ├── Порт: 8000
    ├── Подключение: db:5432
    └── Volume: ./backend (hot-reload)
```

---

## 🔥 Полная очистка (если нужно начать заново)

### Остановить и удалить всё:
```bash
docker-compose down -v  # -v удаляет volumes (БД будет очищена!)
```

### Удалить образы:
```bash
docker-compose down --rmi all
```

### Начать заново:
```bash
docker-compose up -d --build
```

---

## 💡 Советы

### 1. Hot Reload
Backend автоматически перезагружается при изменении Python кода (volume mounted).

### 2. Данные сохраняются
PostgreSQL использует volume `postgres_data` - данные не теряются при перезапуске.

### 3. Быстрая разработка
```bash
# Backend в Docker
docker-compose up -d

# Frontend локально (быстрее hot-reload)
cd frontend && npm run serve
```

---

## ❓ FAQ

### Q: Как изменить порт Backend?

A: В `docker-compose.yml`:
```yaml
ports:
  - "9000:8000"  # localhost:9000 → container:8000
```

### Q: Как сбросить БД?

A:
```bash
docker-compose down -v  # Удалит volume с данными
docker-compose up -d    # Создаст заново
```

### Q: Как посмотреть все таблицы в БД?

A:
```bash
docker exec -it pf-postgres psql -U postgres -d printable_forms -c "\dt"
```

### Q: Можно ли подключиться к БД из DBeaver/pgAdmin?

A: Да!
- Host: `localhost`
- Port: `5432`
- Database: `printable_forms`
- User: `postgres`
- Password: `postgres` (или из .env)

---

## 🎉 Готово!

Теперь запуск занимает **2 команды**:

```bash
./docker-start.sh      # Backend + БД
./frontend-start.sh    # Frontend
```

**Всё работает в Docker! 🐳**

