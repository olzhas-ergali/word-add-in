"""
API endpoints для работы с договорами ДДУ
С поддержкой ДВУХ источников данных:
1. Printable Forms API (по умолчанию)
2. Прямое подключение к БД (если нужна скорость)
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict
from uuid import UUID
import json
from pathlib import Path

from app.models.document import DocumentVariable
from app.services.pf_api_service import PfApiService
from app.services.database_service import db_service

router = APIRouter()

# Загружаем конфигурацию переменных ДДУ
DDU_VARIABLES_PATH = Path(__file__).parent.parent.parent / "variables_export" / "ddu_variables.json"

with open(DDU_VARIABLES_PATH, 'r', encoding='utf-8') as f:
    DDU_CONFIG = json.load(f)


@router.get("/variables")
async def get_ddu_variables():
    """
    Получить все переменные для ДДУ (справочник)
    
    Returns:
        Список всех переменных с их метаданными
    """
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
    """
    Заполнить ДДУ данными из Printable Forms API
    
    Args:
        contract_id: ID договора
        variable_ids: Список ID переменных для заполнения
        
    Returns:
        Словарь {variable_id: value}
    """
    pf_service = PfApiService()
    
    # Получаем значения из API
    variables = await pf_service.get_document_variables_with_values(
        variable_ids=variable_ids,
        token=None  # Или передать токен
    )
    
    # Преобразуем в словарь
    result = {}
    for var in variables:
        result[str(var.id)] = var.value or "Пусто"
    
    return {"variables": result}


@router.post("/fill/database/{contract_id}")
async def fill_ddu_from_database(
    contract_id: str,
    variable_ids: List[str] = None
):
    """
    Заполнить ДДУ данными напрямую из базы данных
    БЫСТРЕЕ чем через API!
    
    Args:
        contract_id: ID договора
        variable_ids: Список ID переменных (опционально, если None - все переменные)
        
    Returns:
        Словарь {variable_id: value}
    """
    
    # Если не указаны переменные, берем все
    if not variable_ids:
        variable_ids = [var['id'] for var in DDU_CONFIG['variables']]
    
    try:
        # Получаем значения из БД
        variables = await db_service.get_variable_values_by_contract(
            contract_id=contract_id,
            variable_ids=variable_ids
        )
        
        # Преобразуем в словарь
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
    """
    Оптимизированное заполнение - один SQL запрос вместо N
    САМЫЙ БЫСТРЫЙ вариант!
    
    Args:
        contract_id: ID договора
        
    Returns:
        Все данные договора
    """
    try:
        # Получаем все данные одним запросом
        contract_data = await db_service.get_contract_data(contract_id)
        
        if not contract_data:
            raise HTTPException(status_code=404, detail="Договор не найден")
        
        # Маппим данные на переменные
        result = {}
        
        for var in DDU_CONFIG['variables']:
            var_id = var['id']
            field_name = var['field']
            
            # Ищем значение в данных договора
            value = contract_data.get(field_name)
            result[var_id] = str(value) if value is not None else "Пусто"
        
        return {
            "variables": result,
            "contract_data": contract_data  # Дополнительно возвращаем все данные
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
    """
    Предпросмотр данных договора
    
    Args:
        contract_id: ID договора
        source: Источник данных ("api" или "database")
        
    Returns:
        Данные для предпросмотра
    """
    if source == "database":
        data = await db_service.get_contract_data(contract_id)
        return {
            "contract_id": contract_id,
            "source": "database",
            "data": data
        }
    else:
        # Через API
        return {
            "contract_id": contract_id,
            "source": "api",
            "message": "Предпросмотр через API - реализуйте по необходимости"
        }

