import httpx
from typing import List, Optional
from uuid import UUID
from io import BytesIO
from app.config import settings
from app.models.document import PfDocument, DocumentVariable


class PfApiService:

    def __init__(self):
        self.base_url = settings.printable_forms_base_url
        self.timeout = 30.0
    
    async def get_template_files(self, token: Optional[str] = None) -> List[PfDocument]:
        if settings.demo_mode or not self.base_url:
            print("🎭 DEMO MODE: Using database instead of API for templates")
            from app.services.database_service import db_service
            templates = await db_service.get_all_templates()
            return templates
        
        url = f"{self.base_url}{settings.printable_forms_get_file_list_api}"
        
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                return [PfDocument(**doc) for doc in data]
                
        except httpx.HTTPError as e:
            print(f"Error fetching template files: {e}")
            return []
    
    async def get_pf_document(self, document_id: UUID, token: Optional[str] = None) -> Optional[bytes]:
        if settings.demo_mode or not self.base_url:
            print(f"🎭 DEMO MODE: Fetching document {document_id} from database")
            from app.services.database_service import db_service
            document_bytes = await db_service.get_template_docx(document_id)
            return document_bytes
        
        url = f"{self.base_url}{settings.printable_forms_get_docx_api}"
        params = {"documentId": str(document_id)}
        
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, params=params, headers=headers)
                response.raise_for_status()
                
                return response.content
                
        except httpx.HTTPError as e:
            print(f"Error fetching document {document_id}: {e}")
            return None
    
    async def get_document_variables(
        self, 
        document_id: UUID, 
        token: Optional[str] = None
    ) -> List[DocumentVariable]:
        if settings.demo_mode or not self.base_url:
            print(f"🎭 DEMO MODE: Fetching variables for document {document_id} from database")
            from app.services.database_service import db_service
            variables = await db_service.get_document_variables(document_id)
            return variables
        
        url = f"{self.base_url}{settings.printable_forms_get_doc_variables_api}"
        params = {"documentId": str(document_id)}
        
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, params=params, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                return [DocumentVariable(**var) for var in data]
                
        except httpx.HTTPError as e:
            print(f"Error fetching document variables: {e}")
            return []
    
    async def get_document_variables_with_values(
        self, 
        variable_ids: List[str], 
        token: Optional[str] = None
    ) -> List[DocumentVariable]:
        if settings.demo_mode or not self.base_url:
            return []
        url = f"{self.base_url}{settings.printable_forms_get_variable_values_api}"
        
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        payload = {"ids": variable_ids}
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, json=payload, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                return [DocumentVariable(**var) for var in data]
                
        except httpx.HTTPError as e:
            print(f"Error fetching variable values: {e}")
            return []

