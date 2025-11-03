import httpx
from typing import List, Optional
from uuid import UUID
from io import BytesIO
from app.config import settings
from app.models.document import PfDocument, DocumentVariable


class PfApiService:
    """Service for Printable Forms API interactions"""
    
    def __init__(self):
        self.base_url = settings.printable_forms_base_url
        self.timeout = 30.0
    
    async def get_template_files(self, token: Optional[str] = None) -> List[PfDocument]:
        """
        Get list of template files
        
        Args:
            token: Optional Bearer token for authentication
            
        Returns:
            List of PfDocument objects
        """
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
        """
        Download document by ID
        
        Args:
            document_id: Document UUID
            token: Optional Bearer token for authentication
            
        Returns:
            Document bytes or None if error
        """
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
        """
        Get document variables by document ID
        
        Args:
            document_id: Document UUID
            token: Optional Bearer token for authentication
            
        Returns:
            List of DocumentVariable objects
        """
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
        """
        Get document variables with values by variable IDs
        
        Args:
            variable_ids: List of variable IDs
            token: Optional Bearer token for authentication
            
        Returns:
            List of DocumentVariable objects with values
        """
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

