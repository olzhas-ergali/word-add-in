@echo off
REM Запуск проекта на Windows
REM Двойной клик на этот файл для запуска

echo =========================================
echo   Запуск Printable Forms Word Add-in
echo =========================================
echo.

REM Проверка Docker
where docker >nul 2>nul
if %errorlevel% neq 0 (
    echo Docker не установлен!
    echo Установите Docker Desktop: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

REM Проверка Node.js
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo Node.js не установлен!
    echo Установите Node.js: https://nodejs.org/
    pause
    exit /b 1
)

echo [OK] Docker установлен
echo [OK] Node.js установлен
echo.

REM Запуск Docker
echo Запуск Backend + PostgreSQL в Docker...
docker-compose up -d

echo Ожидание запуска (15 секунд)...
timeout /t 15 /nobreak >nul

echo.
echo Проверка Backend...
curl -s http://localhost:8000/health >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] Backend запущен на http://localhost:8000
) else (
    echo [ОШИБКА] Backend не запустился!
    echo Проверьте логи: docker-compose logs backend
    pause
    exit /b 1
)

echo.
echo =========================================
echo   Backend готов!
echo =========================================
echo.
echo Теперь запускаю Frontend...
echo.

REM Переход в frontend
cd frontend

REM Проверка node_modules
if not exist "node_modules" (
    echo Установка npm пакетов...
    call npm install
)

REM SSL сертификаты
echo Проверка SSL сертификатов...
call npx office-addin-dev-certs verify >nul 2>nul
if %errorlevel% neq 0 (
    echo Установка SSL сертификатов...
    call npx office-addin-dev-certs install
)

echo.
echo =========================================
echo   ВСЁ ГОТОВО!
echo =========================================
echo.
echo Сервисы:
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
echo Запускаю Frontend dev сервер...
echo.
echo Не закрывайте это окно!
echo.

REM Запуск Frontend
call npm run serve

REM Если пользователь закрыл окно
echo.
echo Frontend остановлен.
echo.
echo Остановить Backend:
echo   docker-compose down
echo.
pause

