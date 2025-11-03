#!/bin/bash

# Скрипт для запуска только Frontend

echo "========================================="
echo "  Запуск Frontend"
echo "========================================="
echo ""

# Проверка Node.js
if ! command -v node &> /dev/null; then
    echo "Node.js не установлен!"
    echo "Установите: https://nodejs.org/"
    exit 1
fi

cd frontend

# Установка зависимостей если нужно
if [ ! -d "node_modules" ]; then
    echo "Установка npm пакетов..."
    npm install
fi

# SSL сертификаты
if ! npx office-addin-dev-certs verify -q 2>/dev/null; then
    echo "Установка SSL сертификатов..."
    npx office-addin-dev-certs install
fi

echo ""
echo "Запуск dev сервера..."
echo ""

npm run serve

