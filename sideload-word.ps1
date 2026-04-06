$ErrorActionPreference = "Stop"
$root = $PSScriptRoot

function Test-DockerStack {
    $fe = docker ps -q -f "name=pf-frontend" -f "status=running" 2>$null
    $be = docker ps -q -f "name=pf-backend" -f "status=running" 2>$null
    if (-not $fe -or -not $be) {
        Write-Host ""
        Write-Host "Контейнеры pf-frontend / pf-backend не запущены." -ForegroundColor Yellow
        Write-Host "Сначала в корне репозитория выполните:" -ForegroundColor Yellow
        Write-Host "  docker compose up -d" -ForegroundColor Cyan
        Write-Host ""
        exit 1
    }
    try {
        $r = Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing -TimeoutSec 10
        if ($r.StatusCode -ne 200) { throw "bad status" }
    } catch {
        Write-Host "Бэкенд не отвечает на http://localhost:8000/health." -ForegroundColor Yellow
        Write-Host "Подождите после docker compose up или выполните: docker compose restart backend" -ForegroundColor Yellow
        exit 1
    }
    $curl = Get-Command curl.exe -ErrorAction SilentlyContinue
    if ($curl) {
        $code = & curl.exe -sk -o NUL -w "%{http_code}" "https://127.0.0.1:3000/" 2>$null
        if ($code -ne "200") {
            Write-Host "Nginx на https://localhost:3000 не отвечает (HTTP $code)." -ForegroundColor Yellow
            Write-Host "Проверьте: docker compose ps   и   docker compose logs frontend" -ForegroundColor Yellow
            exit 1
        }
    }
}

Test-DockerStack

Set-Location (Join-Path $root "frontend")
if (-not (Test-Path "node_modules")) {
    npm install
}
npm run dev:word
