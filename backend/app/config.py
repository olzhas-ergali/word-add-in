from pydantic_settings import BaseSettings
from typing import List, Union


class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_debug: bool = True
    demo_mode: bool = True
    cors_origins: Union[List[str], str] = "*"
    printable_forms_base_url: str = ""
    printable_forms_get_file_list_api: str = "/api/v1/Document/ListMetadata"
    printable_forms_get_docx_api: str = "/api/v1/Document/GetDocx"
    printable_forms_get_doc_variables_api: str = "/api/v1/DocumentVariable/ListByDocumentId"
    printable_forms_get_variable_values_api: str = "/api/v1/DocumentVariable/GetVariableValues"
    keycloak_client_api: str = ""
    keycloak_client_id: str = ""
    keycloak_client_secret: str = ""
    cache_ttl: int = 3600
    database_host: str = "db"
    database_port: int = 5432
    database_name: str = "printable_forms"
    database_user: str = "postgres"
    database_password: str = "postgres"
    use_database_direct: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
