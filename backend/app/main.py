from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import auth, documents, variables


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

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(variables.router, prefix="/api/variables", tags=["Variables"])


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

