from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict
from uuid import UUID
import json
from pathlib import Path

from app.config import settings
from app.models.document import DocumentVariable
from app.services.pf_api_service import PfApiService
from app.services.database_service import db_service
from app.constants import ENCODING_UTF8

router = APIRouter()

DDU_VARIABLES_PATH = Path(__file__).parent.parent.parent.parent / "variables_export" / "ddu_variables.json"
_DDU_CONFIG_CACHE = None


def _get_ddu_config():
    global _DDU_CONFIG_CACHE
    if _DDU_CONFIG_CACHE is not None:
        return _DDU_CONFIG_CACHE
    if not DDU_VARIABLES_PATH.exists():
        return None
    with open(DDU_VARIABLES_PATH, 'r', encoding=ENCODING_UTF8) as f:
        _DDU_CONFIG_CACHE = json.load(f)
    return _DDU_CONFIG_CACHE


@router.get("/variables")
async def get_ddu_variables():
    DDU_CONFIG = _get_ddu_config()
    if DDU_CONFIG is None:
        raise HTTPException(
            status_code=503,
            detail=f"Файл переменных ДДУ не найден: {DDU_VARIABLES_PATH}. Положите ddu_variables.json в variables_export."
        )
    return {
        "document_id": DDU_CONFIG['document_id'],
        "document_name": DDU_CONFIG['document_name'],
        "variables_count": DDU_CONFIG['variables_count'],
        "variables": DDU_CONFIG['variables']
    }


@router.post("/fill/api/{contract_id}")
async def fill_ddu_from_api(
    contract_id: str,
    variable_ids: List[str]
):
    if settings.demo_mode or not settings.printable_forms_base_url:
        DDU_CONFIG = _get_ddu_config()
        if DDU_CONFIG is None:
            raise HTTPException(status_code=503, detail="Файл переменных ДДУ не найден.")
        if not variable_ids:
            variable_ids = [var["id"] for var in DDU_CONFIG["variables"]]
        variables = await db_service.get_variable_values_by_contract(
            contract_id=contract_id,
            variable_ids=variable_ids
        )
        result = {str(var.id): var.value or "Пусто" for var in variables}
        return {"variables": result}
    pf_service = PfApiService()
    variables = await pf_service.get_document_variables_with_values(
        variable_ids=variable_ids,
        token=None
    )
    result = {}
    for var in variables:
        result[str(var.id)] = var.value or "Пусто"
    return {"variables": result}


@router.post("/fill/database/{contract_id}")
async def fill_ddu_from_database(
    contract_id: str,
    variable_ids: List[str] = None
):
    DDU_CONFIG = _get_ddu_config()
    if DDU_CONFIG is None:
        raise HTTPException(status_code=503, detail="Файл переменных ДДУ не найден.")
    if not variable_ids:
        variable_ids = [var['id'] for var in DDU_CONFIG['variables']]

    try:
        variables = await db_service.get_variable_values_by_contract(
            contract_id=contract_id,
            variable_ids=variable_ids
        )
        result = {}
        for var in variables:
            result[str(var.id)] = var.value or "Пусто"
        return {"variables": result}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка получения данных из БД: {str(e)}"
        )


@router.get("/fill/database/optimized/{contract_id}")
async def fill_ddu_optimized(contract_id: str):
    DDU_CONFIG = _get_ddu_config()
    if DDU_CONFIG is None:
        raise HTTPException(status_code=503, detail="Файл переменных ДДУ не найден.")
    try:
        contract_data = await db_service.get_contract_data(contract_id)
        if not contract_data:
            raise HTTPException(status_code=404, detail="Договор не найден")
        result = {}
        for var in DDU_CONFIG['variables']:
            var_id = var['id']
            field_name = var['field']
            value = contract_data.get(field_name)
            result[var_id] = str(value) if value is not None else "Пусто"
        return {
            "variables": result,
            "contract_data": contract_data
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка: {str(e)}"
        )


@router.get("/preview/{contract_id}")
async def preview_contract(
    contract_id: str,
    source: str = Query("database", enum=["api", "database"])
):
    if source == "database":
        data = await db_service.get_contract_data(contract_id)
        return {
            "contract_id": contract_id,
            "source": "database",
            "data": data
        }
    else:
        return {
            "contract_id": contract_id,
            "source": "api",
            "message": "Предпросмотр через API - реализуйте по необходимости"
        }
