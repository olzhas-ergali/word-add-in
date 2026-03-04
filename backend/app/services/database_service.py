from typing import List, Dict, Optional
from uuid import UUID
import asyncpg
from app.config import settings
from app.models.document import DocumentVariable, PfDocument
from datetime import datetime


class DatabaseService:

    def __init__(self):
        self.db_host = settings.database_host
        self.db_port = settings.database_port
        self.db_name = settings.database_name
        self.db_user = settings.database_user
        self.db_password = settings.database_password
        self.pool = None
    
    async def connect(self):
        self.pool = await asyncpg.create_pool(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            min_size=5,
            max_size=20
        )
    
    async def disconnect(self):
        """Закрыть пул подключений"""
        if self.pool:
            await self.pool.close()
    
    async def get_all_templates(self) -> List[PfDocument]:
        if not self.pool:
            await self.connect()
        
        templates = []
        
        async with self.pool.acquire() as conn:
            query = """
                SELECT id, name, file_name, created_at
                FROM documents
                ORDER BY created_at DESC
            """
            
            rows = await conn.fetch(query)
            
            for row in rows:
                templates.append(PfDocument(
                    document_id=UUID(row['id']),
                    document_name=row['name'],
                    file_name=row['file_name'] or f"{row['name']}.docx",
                    created_at=row['created_at'] if row['created_at'] else datetime.now(),
                    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                ))
        
        return templates
    
    async def get_document_variables(self, document_id: UUID) -> List[DocumentVariable]:
        if not self.pool:
            await self.connect()
        
        variables = []
        
        async with self.pool.acquire() as conn:
            query = """
                SELECT 
                    id, document_id, name, display_name, display_name_kz,
                    description, table_name, field_name, data_type,
                    required, example, category
                FROM document_variables
                WHERE document_id = $1
                ORDER BY category, name
            """
            
            rows = await conn.fetch(query, str(document_id))
            
            for row in rows:
                data_type = row['data_type']
                if data_type == 'string':
                    var_type = 'Text'
                elif data_type == 'number':
                    var_type = 'Number'
                elif data_type == 'date':
                    var_type = 'Date'
                elif data_type == 'text':
                    var_type = 'Text'
                else:
                    var_type = 'Text'
                
                variables.append(DocumentVariable(
                    id=UUID(row['id']),
                    table=row['table_name'],
                    field=row['field_name'],
                    name=row['name'],
                    display_name=row['display_name'],
                    display_name_kz=row['display_name_kz'],
                    description=row['description'],
                    category=row['category'],
                    data_type=row['data_type'],
                    required=row['required'] if row['required'] is not None else False,
                    example=row['example'],
                    value=None
                ))
        
        return variables
    
    async def get_template_docx(self, document_id: UUID) -> Optional[bytes]:
        import os
        possible_paths = [
            '/app/ДДУ Шымкент.docx',
            os.path.join(os.path.dirname(__file__), '../../ДДУ Шымкент.docx'),
            '/app/backend/ДДУ Шымкент.docx',
        ]
        
        for file_path in possible_paths:
            if os.path.exists(file_path):
                print(f"✅ Found document file: {file_path}")
                with open(file_path, 'rb') as f:
                    return f.read()
        
        print(f"⚠️ Warning: Document file not found. Tried paths:")
        for path in possible_paths:
            print(f"   - {path}")
        return None
    
    async def get_variable_values_by_contract(
        self, 
        contract_id: str, 
        variable_ids: List[str]
    ) -> List[DocumentVariable]:
        if not self.pool:
            await self.connect()
        
        variables = []
        
        async with self.pool.acquire() as conn:
            query_mapping = """
                SELECT id, name, table_name, field_name, display_name
                FROM document_variables
                WHERE id = ANY($1::uuid[])
            """
            
            mappings = await conn.fetch(query_mapping, variable_ids)
            
            for mapping in mappings:
                var_id = mapping['id']
                table_name = mapping['table_name']
                field_name = mapping['field_name']
                display_name = mapping['display_name']
                
                value = await self._get_value_from_table(
                    conn, 
                    table_name, 
                    field_name, 
                    contract_id
                )
                
                variables.append(DocumentVariable(
                    id=var_id,
                    name=mapping['name'],
                    display_name=display_name,
                    table=table_name,
                    field=field_name,
                    value=value or "Пусто"
                ))
        
        return variables
    
    async def _get_value_from_table(
        self, 
        conn, 
        table_name: str, 
        field_name: str, 
        contract_id: str
    ) -> Optional[str]:
        if not table_name or not field_name:
            return None
        
        try:
            if table_name == 'contracts':
                query = f"""
                    SELECT {field_name}
                    FROM contracts
                    WHERE id = $1
                """
                result = await conn.fetchval(query, contract_id)
                
            elif table_name == 'clients':
                query = f"""
                    SELECT c.{field_name}
                    FROM clients c
                    JOIN contracts ct ON ct.client_id = c.id
                    WHERE ct.id = $1
                """
                result = await conn.fetchval(query, contract_id)
                
            elif table_name == 'apartments':
                query = f"""
                    SELECT a.{field_name}
                    FROM apartments a
                    JOIN contracts ct ON ct.apartment_id = a.id
                    WHERE ct.id = $1
                """
                result = await conn.fetchval(query, contract_id)
                
            elif table_name == 'companies':
                query = f"""
                    SELECT co.{field_name}
                    FROM companies co
                    JOIN contracts ct ON ct.company_id = co.id
                    WHERE ct.id = $1
                """
                result = await conn.fetchval(query, contract_id)
                
            elif table_name == 'buildings':
                query = f"""
                    SELECT b.{field_name}
                    FROM buildings b
                    JOIN apartments a ON a.building_id = b.id
                    JOIN contracts ct ON ct.apartment_id = a.id
                    WHERE ct.id = $1
                """
                result = await conn.fetchval(query, contract_id)
                
            else:
                query = f"""
                    SELECT {field_name}
                    FROM {table_name}
                    WHERE contract_id = $1
                """
                result = await conn.fetchval(query, contract_id)
            
            return str(result) if result is not None else None
            
        except Exception as e:
            print(f"Error getting value from {table_name}.{field_name}: {e}")
            return None
    
    async def get_contract_data(self, contract_id: str) -> Dict:
        if not self.pool:
            await self.connect()
        
        async with self.pool.acquire() as conn:
            query = """
                SELECT
                    ct.id as contract_id,
                    ct.contract_number,
                    ct.contract_date,
                    ct.contract_place,
                    ct.price_total,
                    ct.price_per_meter,
                    ct.completion_date,
                    cl.full_name as client_fio,
                    cl.iin as client_iin,
                    cl.address as client_address,
                    cl.phone as client_phone,
                    cl.email as client_email,
                    cl.passport_number as client_passport,
                    ap.apartment_number,
                    ap.floor as apartment_floor,
                    ap.total_area as apartment_area,
                    ap.rooms_count as apartment_rooms,
                    b.address as building_address,
                    b.cadastral_number as building_cadastral,
                    co.company_name,
                    co.bin as company_bin,
                    co.director_name as company_director,
                    co.legal_address as company_address,
                    co.phone as company_phone,
                    co.bank_name as company_bank,
                    co.account_number as company_account
                FROM contracts ct
                LEFT JOIN clients cl ON ct.client_id = cl.id
                LEFT JOIN apartments ap ON ct.apartment_id = ap.id
                LEFT JOIN buildings b ON ap.building_id = b.id
                LEFT JOIN companies co ON ct.company_id = co.id
                WHERE ct.id = $1
            """
            
            row = await conn.fetchrow(query, contract_id)
            
            if not row:
                return {}
            
            return dict(row)


db_service = DatabaseService()

