from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class PfDocument(BaseModel):
    """Printable Forms document metadata"""
    
    document_id: UUID = Field(..., alias="documentId", description="Unique document identifier")
    document_name: Optional[str] = Field(None, alias="documentName", description="Document display name")
    file_name: str = Field(..., alias="fileName", description="Document file name")
    link: Optional[str] = Field(None, description="Document download link")
    content_type: str = Field(default="application/vnd.openxmlformats-officedocument.wordprocessingml.document", alias="contentType", description="MIME type of the document")
    created_at: datetime = Field(default_factory=datetime.now, alias="createdAt", description="Document creation timestamp")
    organization_name: Optional[str] = Field(None, alias="organizationName", description="Organization name")
    
    class Config:
        populate_by_name = True


class DocumentVariable(BaseModel):
    """Document variable with metadata"""
    
    id: UUID = Field(..., description="Variable unique identifier")
    table: Optional[str] = Field(None, description="Database table name")
    field: Optional[str] = Field(None, description="Database field name")
    name: str = Field(..., description="Variable system name (e.g. CONTRACT_NUMBER)")
    display_name: Optional[str] = Field(None, alias="displayName", description="Русское название переменной")
    display_name_kz: Optional[str] = Field(None, alias="displayNameKz", description="Казахское название")
    description: Optional[str] = Field(None, description="Описание переменной")
    category: Optional[str] = Field(None, description="Категория переменной")
    data_type: Optional[str] = Field(None, alias="dataType", description="Тип данных")
    required: Optional[bool] = Field(None, description="Обязательное поле")
    example: Optional[str] = Field(None, description="Пример значения")
    value: Optional[str] = Field(None, description="Variable value")
    
    class Config:
        populate_by_name = True

