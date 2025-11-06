#!/bin/bash

# Скрипт для запуска frontend с HTTPS для Word Online

echo "🚀 Запуск frontend для Word Online (HTTPS)..."

cd "$(dirname "$0")/frontend"

# Проверка наличия http-server
if ! command -v http-server &> /dev/null; then
    echo "📦 Установка http-server..."
    npm install -g http-server
fi

# Проверка наличия сертификатов
if [ ! -f "localhost.pem" ] || [ ! -f "localhost-key.pem" ]; then
    echo "⚠️  Сертификаты не найдены!"
    echo ""
    echo "Для Word Online требуются HTTPS сертификаты."
    echo ""
    echo "Вариант 1: Использовать http-server без сертификатов (менее безопасно):"
    echo "  npx http-server -p 3000 --ssl --cors"
    echo ""
    echo "Вариант 2: Создать сертификаты с mkcert:"
    echo "  brew install mkcert"
    echo "  mkcert -install"
    echo "  cd frontend"
    echo "  mkcert localhost 127.0.0.1 ::1"
    echo ""
    read -p "Продолжить без сертификатов? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
    
    echo "✅ Запуск без custom сертификатов..."
    npx http-server -p 3000 --ssl --cors
else
    echo "✅ Сертификаты найдены!"
    echo "📂 Запуск с сертификатами..."
    npx http-server -p 3000 --ssl --cert localhost.pem --key localhost-key.pem --cors
fi

echo ""
echo "🎉 Frontend запущен на https://localhost:3000"
echo ""
echo "📋 Следующие шаги:"
echo "1. Откройте https://localhost:3000 в браузере"
echo "2. Добавьте исключение безопасности (если требуется)"
echo "3. Откройте Word Online: https://word.cloud.microsoft.com"
echo "4. Загрузите manifest.xml через Вставка → Надстройки → Мои надстройки"
echo ""

