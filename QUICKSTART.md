# 🚀 Быстрый старт за 5 минут

## Предварительные требования

- ✅ Docker установлен
- ✅ Node.js 18+ установлен
- ✅ Microsoft Word (любая версия)

## Шаг 1: Настройка переменных окружения

```bash
# Скопируйте пример конфигурации
cp .env.example .env

# Отредактируйте .env и добавьте ваш KeyCloak secret
nano .env  # или используйте любой редактор
```

## Шаг 2: Запуск Backend

```bash
# Запустите backend через Docker
./start.sh

# Или вручную:
docker-compose up -d
```

Backend запустится на `http://localhost:8000`

Проверьте: откройте http://localhost:8000/docs в браузере

## Шаг 3: Настройка Frontend

```bash
cd frontend

# Установите зависимости
npm install

# Сгенерируйте SSL сертификаты для разработки
npx office-addin-dev-certs install

# Запустите dev сервер
npm run serve
```

Frontend запустится на `https://localhost:3000`

## Шаг 4: Загрузка Add-in в Word

### Windows

1. Откройте Word
2. Перейдите: **Вставка** → **Надстройки** → **Мои надстройки**
3. Нажмите **Отправить мою надстройку**
4. Выберите файл `frontend/manifest.xml`
5. Нажмите **ОК**

### Mac

1. Откройте Word
2. Перейдите: **Insert** → **Add-ins** → **My Add-ins**
3. Нажмите **Upload My Add-in**
4. Выберите файл `frontend/manifest.xml`
5. Нажмите **Upload**

### Word Online

1. Откройте документ в Word Online
2. Перейдите: **Insert** → **Office Add-ins**
3. Нажмите **Upload My Add-in**
4. Выберите файл `frontend/manifest.xml`
5. Нажмите **Upload**

## Шаг 5: Использование

### 5.1 Вход в систему

1. На ленте Word найдите группу **"Печатные формы"**
2. Нажмите кнопку **"Войти"**
3. Введите ваши учетные данные KeyCloak
4. Нажмите **"Войти"**

### 5.2 Выбор шаблона

1. Нажмите кнопку **"Выбрать шаблон"**
2. Выберите документ из списка
3. Нажмите **"Выбрать"**
4. Документ откроется в Word

### 5.3 Заполнение данных

1. Нажмите кнопку **"Заполнить данные"**
2. Переменные автоматически заполнятся значениями

### 5.4 Выход

1. Нажмите кнопку **"Выйти"**

## 🎉 Готово!

Вы успешно запустили Printable Forms Word Add-in!

## Проблемы?

### Backend не запускается

```bash
# Проверьте логи
docker-compose logs backend

# Проверьте, что порт 8000 свободен
lsof -i :8000

# Перезапустите
docker-compose restart
```

### Frontend не загружается

```bash
# Проверьте, что порт 3000 свободен
lsof -i :3000

# Переустановите зависимости
rm -rf node_modules package-lock.json
npm install

# Проверьте сертификаты
npx office-addin-dev-certs verify
```

### Add-in не появляется в Word

1. Закройте Word полностью
2. Очистите кеш Office:
   - Windows: `%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\`
   - Mac: `~/Library/Containers/com.microsoft.Word/Data/Library/Caches/`
3. Перезапустите Word
4. Загрузите манифест заново

### Ошибки аутентификации

1. Проверьте `.env` файл
2. Убедитесь, что `KEYCLOAK_CLIENT_SECRET` правильный
3. Проверьте доступность KeyCloak сервера
4. Проверьте логи backend: `docker-compose logs backend`

## Дополнительная информация

- 📖 Полная документация: [README-NEW.md](README-NEW.md)
- 🔄 Гайд по миграции: [MIGRATION.md](MIGRATION.md)
- 🐛 Сообщить о проблеме: [GitHub Issues](https://github.com/your-repo/issues)

## Остановка сервисов

```bash
# Остановить все сервисы
./stop.sh

# Или вручную:
docker-compose down

# В frontend директории нажмите Ctrl+C чтобы остановить dev сервер
```

---

**Нужна помощь?** Напишите: support@example.com

