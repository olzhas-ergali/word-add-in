from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class PfDocument(BaseModel):
    """Printable Forms document metadata"""
    
    document_id: UUID = Field(..., alias="documentId", description="Unique document identifier")
    file_name: str = Field(..., alias="fileName", description="Document file name")
    link: Optional[str] = Field(None, description="Document download link")
    content_type: str = Field(..., alias="contentType", description="MIME type of the document")
    created_at: datetime = Field(..., alias="createdAt", description="Document creation timestamp")
    organization_name: Optional[str] = Field(None, alias="organizationName", description="Organization name")
    
    class Config:
        populate_by_name = True


class DocumentVariable(BaseModel):
    """Document variable with metadata"""
    
    id: UUID = Field(..., description="Variable unique identifier")
    table: Optional[str] = Field(None, description="Database table name")
    field: Optional[str] = Field(None, description="Database field name")
    name: str = Field(..., description="Variable display name")
    value: Optional[str] = Field(None, description="Variable value")
    
    class Config:
        populate_by_name = True

