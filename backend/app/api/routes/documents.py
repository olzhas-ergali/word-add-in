from fastapi import APIRouter, HTTPException, Header
from fastapi.responses import StreamingResponse
from typing import List, Optional
from uuid import UUID
from io import BytesIO
from app.models.document import PfDocument
from app.services.pf_api_service import PfApiService
from app.services.cache_service import cache_service

router = APIRouter()


def get_token_from_session(session_id: Optional[str]) -> Optional[str]:
    """Helper to get token from session"""
    if not session_id:
        return None
    
    token_obj = cache_service.get_token(session_id)
    return token_obj.access_token if token_obj else None


@router.get("/list", response_model=List[PfDocument])
async def get_document_list(session_id: Optional[str] = Header(None, alias="X-Session-ID")):
    """
    Get list of available template documents
    
    Args:
        session_id: Optional session ID for authentication
        
    Returns:
        List of PfDocument objects
    """
    pf_service = PfApiService()
    token = get_token_from_session(session_id)
    
    documents = await pf_service.get_template_files(token)
    
    return documents


@router.get("/download/{document_id}")
async def download_document(
    document_id: UUID,
    session_id: Optional[str] = Header(None, alias="X-Session-ID")
):
    """
    Download document by ID
    
    Args:
        document_id: Document UUID
        session_id: Optional session ID for authentication
        
    Returns:
        Document file as streaming response
    """
    pf_service = PfApiService()
    token = get_token_from_session(session_id)
    
    document_bytes = await pf_service.get_pf_document(document_id, token)
    
    if not document_bytes:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return StreamingResponse(
        BytesIO(document_bytes),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f"attachment; filename=document_{document_id}.docx"
        }
    )


@router.get("/{document_id}/metadata", response_model=dict)
async def get_document_metadata(
    document_id: UUID,
    session_id: Optional[str] = Header(None, alias="X-Session-ID")
):
    """
    Get document metadata
    
    Args:
        document_id: Document UUID
        session_id: Optional session ID for authentication
        
    Returns:
        Document metadata
    """
    pf_service = PfApiService()
    token = get_token_from_session(session_id)
    
    # Get all documents and find the requested one
    documents = await pf_service.get_template_files(token)
    document = next((doc for doc in documents if doc.document_id == document_id), None)
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return document.model_dump()

