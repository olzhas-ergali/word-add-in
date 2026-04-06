@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0sideload-word.ps1"
if errorlevel 1 exit /b 1
endlocal
