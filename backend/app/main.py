from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import auth, documents, variables, ddu
from app.services.database_service import db_service


app = FastAPI(
    title="Printable Forms Word Add-in API",
    description="Backend API для Word Add-in с поддержкой KeyCloak аутентификации",
    version="1.0.0",
    debug=settings.api_debug
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database lifecycle
@app.on_event("startup")
async def startup():
    """Подключение к БД при старте (если используется прямое подключение)"""
    if settings.use_database_direct:
        await db_service.connect()

@app.on_event("shutdown")
async def shutdown():
    """Закрытие подключения к БД"""
    if settings.use_database_direct:
        await db_service.disconnect()

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(variables.router, prefix="/api/variables", tags=["Variables"])
app.include_router(ddu.router, prefix="/api/ddu", tags=["ДДУ"])  # Новый роутер!


@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "Printable Forms Word Add-in API is running",
        "version": "1.0.0"
    }


@app.get("/health", tags=["Health"])
async def health():
    """Detailed health check"""
    return {
        "status": "healthy",
        "api_version": "1.0.0",
        "keycloak_configured": bool(settings.keycloak_client_api),
        "printable_forms_configured": bool(settings.printable_forms_base_url)
    }

