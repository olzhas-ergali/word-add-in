@echo off
REM Установка надстройки в Desktop Word на Windows
REM Двойной клик на этот файл

echo =========================================
echo   Установка надстройки в Word
echo =========================================
echo.

REM Получить путь к скрипту
set SCRIPT_DIR=%~dp0

REM Создать папку для надстроек
set WEF_DIR=%LOCALAPPDATA%\Microsoft\Office\16.0\Wef
echo Создание папки: %WEF_DIR%
mkdir "%WEF_DIR%" 2>nul

REM Скопировать манифест
echo Копирование manifest.xml...
copy /Y "%SCRIPT_DIR%frontend\manifest.xml" "%WEF_DIR%\"

if %errorlevel% equ 0 (
    echo [OK] Манифест скопирован!
) else (
    echo [ОШИБКА] Не удалось скопировать манифест!
    pause
    exit /b 1
)

echo.
echo =========================================
echo   Манифест установлен!
echo =========================================
echo.
echo ТЕПЕРЬ НАСТРОЙТЕ WORD:
echo.
echo 1. Откройте Word
echo.
echo 2. Файл - Параметры
echo.
echo 3. Центр управления безопасностью
echo    - Параметры центра управления безопасностью...
echo.
echo 4. Надежные каталоги надстроек
echo    - В поле "URL каталога" вставьте:
echo      %WEF_DIR%
echo.
echo    - Нажмите "Добавить каталог"
echo    - Поставьте галочку "Показывать в меню"
echo.
echo 5. Нажмите ОК - ОК
echo.
echo 6. Закройте Word полностью (Alt+F4)
echo.
echo 7. Откройте Word заново
echo.
echo 8. Вставка - Надстройки - Мои надстройки - ОБЩАЯ ПАПКА
echo.
echo Там будет ваша надстройка!
echo.
echo =========================================
echo.
echo АЛЬТЕРНАТИВА (проще):
echo.
echo Используйте Word Online:
echo 1. Откройте https://office.com
echo 2. Word Online - Новый документ
echo 3. Вставка - Надстройки Office
echo 4. "Отправить мою надстройку"
echo 5. Выберите manifest.xml
echo.
echo =========================================
echo.
pause

