from fastapi import APIRouter, HTTPException, Header
from typing import List, Optional
from uuid import UUID
from app.models.document import DocumentVariable
from app.models.requests import VariableValuesRequest
from app.services.pf_api_service import PfApiService
from app.services.cache_service import cache_service

router = APIRouter()


def get_token_from_session(session_id: Optional[str]) -> Optional[str]:
    if not session_id:
        return None
    
    token_obj = cache_service.get_token(session_id)
    return token_obj.access_token if token_obj else None


@router.get("/document/{document_id}", response_model=List[DocumentVariable])
async def get_document_variables(
    document_id: UUID,
    session_id: Optional[str] = Header(None, alias="X-Session-ID")
):
    pf_service = PfApiService()
    token = get_token_from_session(session_id)
    
    variables = await pf_service.get_document_variables(document_id, token)
    
    return variables


@router.post("/values", response_model=List[DocumentVariable])
async def get_variable_values(
    request: VariableValuesRequest,
    session_id: Optional[str] = Header(None, alias="X-Session-ID")
):
    if not request.ids:
        raise HTTPException(status_code=400, detail="No variable IDs provided")
    
    pf_service = PfApiService()
    token = get_token_from_session(session_id)
    
    variables = await pf_service.get_document_variables_with_values(request.ids, token)
    
    return variables

