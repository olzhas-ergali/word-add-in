echo "========================================="
echo "  Запуск Printable Forms Word Add-in"
echo "========================================="
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Функция для вывода с цветом
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${YELLOW}→${NC} $1"
}

# ============================================
# 1. ПРОВЕРКА ЗАВИСИМОСТЕЙ
# ============================================

echo "Шаг 1: Проверка зависимостей..."
echo ""

# Проверка Docker
if ! command -v docker &> /dev/null; then
    print_error "Docker не установлен!"
    echo "   Установите Docker Desktop: https://www.docker.com/products/docker-desktop"
    exit 1
fi
print_success "Docker установлен"

# Проверка Node.js
if ! command -v node &> /dev/null; then
    print_error "Node.js не установлен!"
    echo "   Установите Node.js: https://nodejs.org/"
    exit 1
fi
print_success "Node.js установлен"

# Проверка что Docker запущен
if ! docker info &> /dev/null; then
    print_error "Docker не запущен!"
    echo "   Запустите Docker Desktop и попробуйте снова"
    exit 1
fi
print_success "Docker запущен"

echo ""

# ============================================
# 2. НАСТРОЙКА .ENV
# ============================================

echo "Шаг 2: Проверка конфигурации..."
echo ""

if [ ! -f ".env" ]; then
    print_info "Создание .env файла..."
    cat > .env << 'EOF'
# Database
DATABASE_PASSWORD=postgres

# Printable Forms API
PRINTABLE_FORMS_BASE_URL=https://apigw.test.bi.group/printable-forms

# KeyCloak (не используется, но нужно для запуска)
KEYCLOAK_CLIENT_API=https://sso.test.bi.group/realms/bi-group/protocol/openid-connect/token
KEYCLOAK_CLIENT_ID=printable-forms
KEYCLOAK_CLIENT_SECRET=Bcb3NYb5JtFhKKuB2whG0TyxSB2NvR0t
EOF
    print_success ".env файл создан"
else
    print_success ".env файл существует"
fi

echo ""

# ============================================
# 3. ЗАПУСК DOCKER (Backend + PostgreSQL)
# ============================================

echo "Шаг 3: Запуск Backend + PostgreSQL в Docker..."
echo ""

print_info "Остановка старых контейнеров (если есть)..."
docker-compose down &> /dev/null

print_info "Запуск docker-compose..."
docker-compose up -d --build

if [ $? -ne 0 ]; then
    print_error "Ошибка запуска Docker!"
    echo "   Проверьте логи: docker-compose logs"
    exit 1
fi

print_info "Ожидание запуска сервисов (15 секунд)..."
sleep 15

# Проверка Backend
print_info "Проверка Backend..."
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    print_success "Backend запущен на http://localhost:8000"
else
    print_error "Backend не запустился!"
    echo "   Проверьте логи: docker-compose logs backend"
    exit 1
fi

# Проверка PostgreSQL
print_info "Проверка PostgreSQL..."
if docker exec pf-postgres pg_isready -U postgres &> /dev/null; then
    print_success "PostgreSQL запущен (порт 5432)"
else
    print_error "PostgreSQL не запустился!"
    echo "   Проверьте логи: docker-compose logs db"
    exit 1
fi

echo ""

# ============================================
# 4. ЗАПУСК FRONTEND
# ============================================

echo "Шаг 4: Запуск Frontend..."
echo ""

cd frontend

# Проверка node_modules
if [ ! -d "node_modules" ]; then
    print_info "Установка npm пакетов (это может занять минуту)..."
    npm install --silent
    if [ $? -ne 0 ]; then
        print_error "Ошибка установки npm пакетов!"
        exit 1
    fi
    print_success "NPM пакеты установлены"
else
    print_success "NPM пакеты уже установлены"
fi

# SSL сертификаты
print_info "Проверка SSL сертификатов..."
if ! npx office-addin-dev-certs verify -q 2>/dev/null; then
    print_info "Установка SSL сертификатов (может потребовать пароль)..."
    npx office-addin-dev-certs install
    if [ $? -ne 0 ]; then
        print_error "Ошибка установки SSL сертификатов!"
        echo "   Попробуйте вручную: npx office-addin-dev-certs install"
        exit 1
    fi
    print_success "SSL сертификаты установлены"
else
    print_success "SSL сертификаты уже установлены"
fi

echo ""
echo "========================================="
echo "  ВСЁ ГОТОВО К ЗАПУСКУ!"
echo "========================================="
echo ""
print_success "Backend:     http://localhost:8000"
print_success "API Docs:    http://localhost:8000/docs"
print_success "PostgreSQL:  localhost:5432"
echo ""
print_info "Запускаю Frontend dev сервер..."
echo ""
echo "========================================="
echo ""

# Запуск Frontend
# Используем exec чтобы сигналы (Ctrl+C) работали правильно
exec npm run serve
