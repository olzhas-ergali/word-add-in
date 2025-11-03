from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_debug: bool = True
    
    # CORS Settings
    cors_origins: List[str] = [
        "http://localhost:8000",   # Backend для self-requests
        "https://localhost:8000",  # Backend HTTPS
        "http://localhost:3000",   # Frontend HTTP (development)
        "https://localhost:3000",  # Frontend HTTPS (production)
        "https://localhost:3001",  # Альтернативный frontend порт
    ]
    
    # Printable Forms API
    printable_forms_base_url: str
    printable_forms_get_file_list_api: str = "/api/v1/Document/ListMetadata"
    printable_forms_get_docx_api: str = "/api/v1/Document/GetDocx"
    printable_forms_get_doc_variables_api: str = "/api/v1/DocumentVariable/ListByDocumentId"
    printable_forms_get_variable_values_api: str = "/api/v1/DocumentVariable/GetVariableValues"
    
    # KeyCloak Configuration
    keycloak_client_api: str
    keycloak_client_id: str
    keycloak_client_secret: str
    
    # Cache Settings
    cache_ttl: int = 3600
    
    # Database Configuration (для прямого подключения)
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "printable_forms"
    database_user: str = "postgres"
    database_password: str = "password"
    use_database_direct: bool = False  # Флаг: использовать ли прямое подключение к БД
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
