#!/bin/bash

# Простой скрипт запуска всего в Docker

echo "========================================="
echo "  Запуск Printable Forms Word Add-in"
echo "========================================="
echo ""

# Проверка Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не установлен!"
    echo "Установите Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "1. Запуск Docker контейнеров..."
echo ""

# Запуск docker-compose
docker-compose up -d

echo ""
echo "2. Ожидание запуска сервисов..."
sleep 5

# Проверка backend
echo ""
echo "3. Проверка Backend..."
if curl -s http://localhost:8000/health > /dev/null; then
    echo "   Backend: OK"
else
    echo "   Backend: Ошибка (смотрите логи: docker-compose logs backend)"
fi

# Проверка БД
echo ""
echo "4. Проверка PostgreSQL..."
if docker exec pf-postgres pg_isready -U postgres > /dev/null 2>&1; then
    echo "   PostgreSQL: OK"
else
    echo "   PostgreSQL: Ошибка (смотрите логи: docker-compose logs db)"
fi

echo ""
echo "========================================="
echo "  Backend готов!"
echo "========================================="
echo ""
echo "Сервисы:"
echo "  Backend API:  http://localhost:8000"
echo "  API Docs:     http://localhost:8000/docs"
echo "  PostgreSQL:   localhost:5432"
echo ""
echo "Теперь запустите Frontend:"
echo "  cd frontend"
echo "  npm install"
echo "  npm run serve"
echo ""
echo "Или используйте готовый скрипт:"
echo "  ./frontend-start.sh"
echo ""
echo "Логи backend: docker-compose logs -f backend"
echo "Остановка:    docker-compose down"
echo ""

