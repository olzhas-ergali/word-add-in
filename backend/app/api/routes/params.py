from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from app.services.database_service import db_service

router = APIRouter()


class Parameter(BaseModel):
    id: Optional[int] = None
    contract_id: str
    param_name: str
    param_value: str
    description: Optional[str] = None


class CreateParameterRequest(BaseModel):
    contract_id: str
    param_name: str
    param_value: str
    description: Optional[str] = None


@router.get("/list")
async def get_all_parameters():
    try:
        if not db_service.pool:
            await db_service.connect()
        
        async with db_service.pool.acquire() as conn:
            query = """
                SELECT 
                    id,
                    contract_id,
                    param_name,
                    param_value,
                    description,
                    created_at,
                    updated_at
                FROM contract_parameters
                ORDER BY created_at DESC
            """
            
            rows = await conn.fetch(query)
            
            return {
                "count": len(rows),
                "parameters": [dict(row) for row in rows]
            }
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка получения параметров: {str(e)}"
        )


@router.get("/contract/{contract_id}")
async def get_parameters_by_contract(contract_id: str):
    try:
        if not db_service.pool:
            await db_service.connect()
        
        async with db_service.pool.acquire() as conn:
            query = """
                SELECT 
                    id,
                    contract_id,
                    param_name,
                    param_value,
                    description,
                    created_at,
                    updated_at
                FROM contract_parameters
                WHERE contract_id = $1
                ORDER BY param_name
            """
            
            rows = await conn.fetch(query, contract_id)
            
            if not rows:
                return {
                    "contract_id": contract_id,
                    "count": 0,
                    "parameters": []
                }
            
            return {
                "contract_id": contract_id,
                "count": len(rows),
                "parameters": [dict(row) for row in rows]
            }
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка получения параметров: {str(e)}"
        )


@router.post("/add")
async def add_parameter(param: CreateParameterRequest):
    try:
        if not db_service.pool:
            await db_service.connect()
        
        async with db_service.pool.acquire() as conn:
            query = """
                INSERT INTO contract_parameters 
                (contract_id, param_name, param_value, description, created_at)
                VALUES ($1, $2, $3, $4, NOW())
                RETURNING id, contract_id, param_name, param_value, description, created_at
            """
            
            row = await conn.fetchrow(
                query,
                param.contract_id,
                param.param_name,
                param.param_value,
                param.description
            )
            
            return {
                "success": True,
                "message": "Параметр добавлен",
                "parameter": dict(row)
            }
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка добавления параметра: {str(e)}"
        )


@router.put("/update/{param_id}")
async def update_parameter(param_id: int, param: CreateParameterRequest):
    try:
        if not db_service.pool:
            await db_service.connect()
        
        async with db_service.pool.acquire() as conn:
            query = """
                UPDATE contract_parameters
                SET 
                    param_name = $1,
                    param_value = $2,
                    description = $3,
                    updated_at = NOW()
                WHERE id = $4
                RETURNING id, contract_id, param_name, param_value, description, updated_at
            """
            
            row = await conn.fetchrow(
                query,
                param.param_name,
                param.param_value,
                param.description,
                param_id
            )
            
            if not row:
                raise HTTPException(status_code=404, detail="Параметр не найден")
            
            return {
                "success": True,
                "message": "Параметр обновлен",
                "parameter": dict(row)
            }
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка обновления параметра: {str(e)}"
        )


@router.delete("/delete/{param_id}")
async def delete_parameter(param_id: int):
    try:
        if not db_service.pool:
            await db_service.connect()
        
        async with db_service.pool.acquire() as conn:
            query = "DELETE FROM contract_parameters WHERE id = $1 RETURNING id"
            
            row = await conn.fetchrow(query, param_id)
            
            if not row:
                raise HTTPException(status_code=404, detail="Параметр не найден")
            
            return {
                "success": True,
                "message": "Параметр удален",
                "deleted_id": row['id']
            }
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка удаления параметра: {str(e)}"
        )


@router.get("/search")
async def search_parameters(
    contract_id: Optional[str] = None,
    param_name: Optional[str] = None,
    param_value: Optional[str] = None
):
    try:
        if not db_service.pool:
            await db_service.connect()
        
        conditions = []
        params = []
        param_counter = 1
        
        if contract_id:
            conditions.append(f"contract_id = ${param_counter}")
            params.append(contract_id)
            param_counter += 1
        
        if param_name:
            conditions.append(f"param_name ILIKE ${param_counter}")
            params.append(f"%{param_name}%")
            param_counter += 1
        
        if param_value:
            conditions.append(f"param_value ILIKE ${param_counter}")
            params.append(f"%{param_value}%")
            param_counter += 1
        
        where_clause = " AND ".join(conditions) if conditions else "1=1"
        
        async with db_service.pool.acquire() as conn:
            query = f"""
                SELECT 
                    id,
                    contract_id,
                    param_name,
                    param_value,
                    description,
                    created_at,
                    updated_at
                FROM contract_parameters
                WHERE {where_clause}
                ORDER BY created_at DESC
                LIMIT 100
            """
            
            rows = await conn.fetch(query, *params)
            
            return {
                "count": len(rows),
                "parameters": [dict(row) for row in rows]
            }
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка поиска параметров: {str(e)}"
        )

