# Устанавливает сертификат nginx из контейнера pf-frontend в хранилище
# «Доверенные корневые центры сертификации», чтобы Word не блокировал надстройку.
#
# По умолчанию — хранилище текущего пользователя (без прав администратора):
#   powershell -ExecutionPolicy Bypass -File .\scripts\trust-localhost-cert.ps1
# Если Word всё ещё ругается на сертификат — повторите с PowerShell «От имени администратора»
# (тот же скрипт добавит сертификат в хранилище локального компьютера).
$ErrorActionPreference = "Stop"

$tmp = Join-Path $env:TEMP "pf-nginx-localhost.crt"
docker cp pf-frontend:/etc/nginx/ssl/localhost.crt $tmp
if (-not (Test-Path $tmp)) {
    Write-Error "Не удалось скопировать сертификат. Запущен ли контейнер? docker compose up -d"
}

$isAdmin = $false
try {
    $isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
        [Security.Principal.WindowsBuiltInRole]::Administrator)
} catch { }

if ($isAdmin) {
    certutil -addstore -f "Root" $tmp
} else {
    certutil -user -addstore -f "Root" $tmp
}
if ($LASTEXITCODE -ne 0) {
    Write-Error "certutil завершился с ошибкой. Если не хватает прав — запустите этот же скрипт в PowerShell от имени администратора."
}

Remove-Item -Force $tmp -ErrorAction SilentlyContinue
Write-Host ""
Write-Host "Готово. Полностью закройте Word (все окна) и перезапустите Word, затем нажмите «Перезапустить» в панели надстройки." -ForegroundColor Green
Write-Host ""
