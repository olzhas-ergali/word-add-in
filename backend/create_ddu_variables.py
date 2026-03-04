import json
from pathlib import Path
from uuid import uuid4
from datetime import datetime

from app.constants import ENCODING_UTF8, ENCODING_UTF8_SIG


def create_ddu_variables():
    document_id = str(uuid4())
    document_name = "ДДУ Шымкент"
    variables = [
        {
            "id": str(uuid4()),
            "name": "CONTRACT_NUMBER",
            "display_name": "Номер договора",
            "display_name_kz": "Шарт нөмірі",
            "description": "Номер договора долевого участия",
            "table": "contracts",
            "field": "contract_number",
            "data_type": "string",
            "required": True,
            "example": "ADL-1-204/41",
            "category": "Договор"
        },
        {
            "id": str(uuid4()),
            "name": "CONTRACT_DATE",
            "display_name": "Дата договора",
            "display_name_kz": "Шарт күні",
            "description": "Дата заключения договора",
            "table": "contracts",
            "field": "contract_date",
            "data_type": "date",
            "required": True,
            "example": "25.02.2020",
            "category": "Договор"
        },
        {
            "id": str(uuid4()),
            "name": "CONTRACT_PLACE",
            "display_name": "Место заключения договора",
            "display_name_kz": "Шарт жасасу орны",
            "description": "Город/место заключения договора",
            "table": "contracts",
            "field": "contract_place",
            "data_type": "string",
            "required": True,
            "example": "г. Нур-Султан",
            "category": "Договор"
        },
        {
            "id": str(uuid4()),
            "name": "CONTRACT_YEAR",
            "display_name": "Год договора",
            "display_name_kz": "Шарт жылы",
            "description": "Год заключения договора",
            "table": "contracts",
            "field": "contract_year",
            "data_type": "number",
            "required": True,
            "example": "2020",
            "category": "Договор"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_NAME",
            "display_name": "Наименование компании",
            "display_name_kz": "Компания атауы",
            "description": "Полное наименование уполномоченной компании",
            "table": "companies",
            "field": "company_name",
            "data_type": "string",
            "required": True,
            "example": "ТОО 'Town House'",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_DIRECTOR",
            "display_name": "Руководитель компании",
            "display_name_kz": "Компания басшысы",
            "description": "ФИО руководителя компании",
            "table": "companies",
            "field": "director_name",
            "data_type": "string",
            "required": True,
            "example": "Иванов Иван Иванович",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_BASIS",
            "display_name": "Основание полномочий",
            "display_name_kz": "Өкілеттік негізі",
            "description": "Документ, на основании которого действует руководитель",
            "table": "companies",
            "field": "authority_basis",
            "data_type": "string",
            "required": True,
            "example": "Устава",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_BIN",
            "display_name": "БИН компании",
            "display_name_kz": "Компанияның БСН",
            "description": "Бизнес-идентификационный номер",
            "table": "companies",
            "field": "bin",
            "data_type": "string",
            "required": True,
            "example": "123456789012",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_ADDRESS",
            "display_name": "Юридический адрес компании",
            "display_name_kz": "Компанияның заңды мекенжайы",
            "description": "Полный юридический адрес",
            "table": "companies",
            "field": "legal_address",
            "data_type": "string",
            "required": True,
            "example": "г. Нур-Султан, ул. Абая, д. 10",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_PHONE",
            "display_name": "Телефон компании",
            "display_name_kz": "Компания телефоны",
            "description": "Контактный телефон",
            "table": "companies",
            "field": "phone",
            "data_type": "string",
            "required": True,
            "example": "+7 (7172) 123-456",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_EMAIL",
            "display_name": "Email компании",
            "display_name_kz": "Компания email",
            "description": "Электронная почта",
            "table": "companies",
            "field": "email",
            "data_type": "string",
            "required": False,
            "example": "info@townhouse.kz",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_BANK",
            "display_name": "Банк компании",
            "display_name_kz": "Компания банкі",
            "description": "Наименование банка",
            "table": "companies",
            "field": "bank_name",
            "data_type": "string",
            "required": True,
            "example": "АО 'Народный Банк Казахстана'",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_ACCOUNT",
            "display_name": "Расчетный счет",
            "display_name_kz": "Есеп шоты",
            "description": "Номер расчетного счета",
            "table": "companies",
            "field": "account_number",
            "data_type": "string",
            "required": True,
            "example": "KZ123456789012345678",
            "category": "Уполномоченная компания"
        },
        {
            "id": str(uuid4()),
            "name": "COMPANY_BIK",
            "display_name": "БИК банка",
            "display_name_kz": "Банктің БСК",
            "description": "БИК банка компании",
            "table": "companies",
            "field": "bik",
            "data_type": "string",
            "required": True,
            "example": "HSBKKZKX",
            "category": "Уполномоченная компания"
        },
        
        {
            "id": str(uuid4()),
            "name": "CLIENT_FIO",
            "display_name": "ФИО дольщика",
            "display_name_kz": "Үлескердің Т.А.Ә.",
            "description": "Полное имя дольщика",
            "table": "clients",
            "field": "full_name",
            "data_type": "string",
            "required": True,
            "example": "Петров Петр Петрович",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_IIN",
            "display_name": "ИИН дольщика",
            "display_name_kz": "Үлескердің ЖСН",
            "description": "Индивидуальный идентификационный номер",
            "table": "clients",
            "field": "iin",
            "data_type": "string",
            "required": True,
            "example": "900101300123",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_ADDRESS",
            "display_name": "Адрес дольщика",
            "display_name_kz": "Үлескердің мекенжайы",
            "description": "Адрес регистрации дольщика",
            "table": "clients",
            "field": "address",
            "data_type": "string",
            "required": True,
            "example": "г. Нур-Султан, ул. Кенесары, д. 5, кв. 10",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_PHONE",
            "display_name": "Телефон дольщика",
            "display_name_kz": "Үлескердің телефоны",
            "description": "Контактный телефон дольщика",
            "table": "clients",
            "field": "phone",
            "data_type": "string",
            "required": True,
            "example": "+7 (777) 123-45-67",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_EMAIL",
            "display_name": "Email дольщика",
            "display_name_kz": "Үлескердің email",
            "description": "Электронная почта дольщика",
            "table": "clients",
            "field": "email",
            "data_type": "string",
            "required": False,
            "example": "petrov@mail.ru",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_PASSPORT",
            "display_name": "Документ удостоверяющий личность",
            "display_name_kz": "Жеке куәлік",
            "description": "Серия и номер документа",
            "table": "clients",
            "field": "passport_number",
            "data_type": "string",
            "required": True,
            "example": "N 12345678",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_PASSPORT_ISSUED_BY",
            "display_name": "Кем выдан документ",
            "display_name_kz": "Құжатты кім берген",
            "description": "Орган, выдавший документ",
            "table": "clients",
            "field": "passport_issued_by",
            "data_type": "string",
            "required": True,
            "example": "МВД РК",
            "category": "Дольщик"
        },
        {
            "id": str(uuid4()),
            "name": "CLIENT_PASSPORT_DATE",
            "display_name": "Дата выдачи документа",
            "display_name_kz": "Құжат берілген күні",
            "description": "Дата выдачи документа",
            "table": "clients",
            "field": "passport_issue_date",
            "data_type": "date",
            "required": True,
            "example": "01.01.2020",
            "category": "Дольщик"
        },
        
        {
            "id": str(uuid4()),
            "name": "APARTMENT_NUMBER",
            "display_name": "Номер квартиры",
            "display_name_kz": "Пәтер нөмірі",
            "description": "Номер квартиры в доме",
            "table": "apartments",
            "field": "apartment_number",
            "data_type": "string",
            "required": True,
            "example": "204",
            "category": "Объект"
        },
        {
            "id": str(uuid4()),
            "name": "APARTMENT_FLOOR",
            "display_name": "Этаж",
            "display_name_kz": "Қабат",
            "description": "Этаж расположения квартиры",
            "table": "apartments",
            "field": "floor",
            "data_type": "number",
            "required": True,
            "example": "5",
            "category": "Объект"
        },
        {
            "id": str(uuid4()),
            "name": "APARTMENT_AREA",
            "display_name": "Общая площадь",
            "display_name_kz": "Жалпы алаң",
            "description": "Общая площадь квартиры в кв.м",
            "table": "apartments",
            "field": "total_area",
            "data_type": "number",
            "required": True,
            "example": "65.5",
            "category": "Объект"
        },
        {
            "id": str(uuid4()),
            "name": "APARTMENT_ROOMS",
            "display_name": "Количество комнат",
            "display_name_kz": "Бөлмелер саны",
            "description": "Количество жилых комнат",
            "table": "apartments",
            "field": "rooms_count",
            "data_type": "number",
            "required": True,
            "example": "2",
            "category": "Объект"
        },
        {
            "id": str(uuid4()),
            "name": "BUILDING_ADDRESS",
            "display_name": "Адрес дома",
            "display_name_kz": "Үйдің мекенжайы",
            "description": "Полный адрес многоквартирного дома",
            "table": "buildings",
            "field": "address",
            "data_type": "string",
            "required": True,
            "example": "г. Шымкент, мкр. Нурсат, ул. Жантокова, д. 1",
            "category": "Объект"
        },
        {
            "id": str(uuid4()),
            "name": "BUILDING_CADASTRAL",
            "display_name": "Кадастровый номер",
            "display_name_kz": "Кадастрлық нөмір",
            "description": "Кадастровый номер здания",
            "table": "buildings",
            "field": "cadastral_number",
            "data_type": "string",
            "required": False,
            "example": "10-111-222-333",
            "category": "Объект"
        },
        
        {
            "id": str(uuid4()),
            "name": "PRICE_TOTAL",
            "display_name": "Стоимость доли",
            "display_name_kz": "Үлестің құны",
            "description": "Полная стоимость доли",
            "table": "contracts",
            "field": "price_total",
            "data_type": "number",
            "required": True,
            "example": "15000000",
            "category": "Финансы"
        },
        {
            "id": str(uuid4()),
            "name": "PRICE_PER_METER",
            "display_name": "Цена за кв.м",
            "display_name_kz": "Шаршы метрдің бағасы",
            "description": "Стоимость одного квадратного метра",
            "table": "contracts",
            "field": "price_per_meter",
            "data_type": "number",
            "required": True,
            "example": "228000",
            "category": "Финансы"
        },
        {
            "id": str(uuid4()),
            "name": "PAYMENT_SCHEDULE",
            "display_name": "График платежей",
            "display_name_kz": "Төлем кестесі",
            "description": "График платежей",
            "table": "contracts",
            "field": "payment_schedule",
            "data_type": "text",
            "required": False,
            "example": "Согласно приложению №3",
            "category": "Финансы"
        },
        
        {
            "id": str(uuid4()),
            "name": "COMPLETION_DATE",
            "display_name": "Срок сдачи дома",
            "display_name_kz": "Үйді тапсыру мерзімі",
            "description": "Планируемая дата сдачи дома",
            "table": "contracts",
            "field": "completion_date",
            "data_type": "date",
            "required": True,
            "example": "31.12.2024",
            "category": "Сроки"
        },
        {
            "id": str(uuid4()),
            "name": "ACCEPTANCE_ACT_NUMBER",
            "display_name": "Номер акта приемки",
            "display_name_kz": "Қабылдау актісінің нөмірі",
            "description": "Номер акта приемки в эксплуатацию",
            "table": "documents",
            "field": "acceptance_act_number",
            "data_type": "string",
            "required": False,
            "example": "АКТ-2024-001",
            "category": "Документы"
        },
        {
            "id": str(uuid4()),
            "name": "ACCEPTANCE_ACT_DATE",
            "display_name": "Дата акта приемки",
            "display_name_kz": "Қабылдау актісінің күні",
            "description": "Дата акта приемки в эксплуатацию",
            "table": "documents",
            "field": "acceptance_act_date",
            "data_type": "date",
            "required": False,
            "example": "15.12.2024",
            "category": "Документы"
        },
        {
            "id": str(uuid4()),
            "name": "REGISTRATION_NUMBER",
            "display_name": "Номер регистрации",
            "display_name_kz": "Тіркеу нөмірі",
            "description": "Номер государственной регистрации",
            "table": "documents",
            "field": "registration_number",
            "data_type": "string",
            "required": False,
            "example": "РЕГ-2024-12345",
            "category": "Документы"
        },
        {
            "id": str(uuid4()),
            "name": "REGISTRATION_DATE",
            "display_name": "Дата регистрации",
            "display_name_kz": "Тіркеу күні",
            "description": "Дата государственной регистрации",
            "table": "documents",
            "field": "registration_date",
            "data_type": "date",
            "required": False,
            "example": "20.12.2024",
            "category": "Документы"
        },
        
        {
            "id": str(uuid4()),
            "name": "KEYS_COUNT",
            "display_name": "Количество ключей",
            "display_name_kz": "Кілттер саны",
            "description": "Количество переданных ключей",
            "table": "contracts",
            "field": "keys_count",
            "data_type": "number",
            "required": True,
            "example": "2",
            "category": "Дополнительно"
        },
        {
            "id": str(uuid4()),
            "name": "WITNESS_NAME",
            "display_name": "ФИО свидетеля",
            "display_name_kz": "Куәгердің Т.А.Ә.",
            "description": "ФИО свидетеля сделки",
            "table": "contracts",
            "field": "witness_name",
            "data_type": "string",
            "required": False,
            "example": "Сидоров Сергей Сергеевич",
            "category": "Дополнительно"
        },
    ]
    
    return document_id, document_name, variables


def save_to_json(document_id, document_name, variables, output_dir):
    output_path = output_dir / "ddu_variables.json"
    
    data = {
        "document_id": document_id,
        "document_name": document_name,
        "created_at": datetime.now().isoformat(),
        "variables_count": len(variables),
        "variables": variables
    }
    
    with open(output_path, 'w', encoding=ENCODING_UTF8) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSON: {output_path}")
    return output_path


def save_to_sql(document_id, document_name, variables, output_dir):
    output_path = output_dir / "ddu_variables.sql"
    
    sql = f"""-- SQL скрипт для документа ДДУ Шымкент
-- Дата создания: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-- Переменных: {len(variables)}

-- Создание таблиц (если не существуют)
CREATE TABLE IF NOT EXISTS documents (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    file_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS document_variables (
    id VARCHAR(36) PRIMARY KEY,
    document_id VARCHAR(36) NOT NULL,
    name VARCHAR(100) NOT NULL,
    display_name VARCHAR(255),
    display_name_kz VARCHAR(255),
    description TEXT,
    table_name VARCHAR(100),
    field_name VARCHAR(100),
    data_type VARCHAR(50),
    required BOOLEAN DEFAULT TRUE,
    example VARCHAR(255),
    category VARCHAR(100),
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

-- Вставка документа
INSERT INTO documents (id, name, file_name, created_at) 
VALUES ('{document_id}', '{document_name}', 'ДДУ Шымкент.docx', NOW())
ON DUPLICATE KEY UPDATE name = '{document_name}';

-- Вставка переменных
"""
    
    for var in variables:
        sql += f"""
INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '{var['id']}',
    '{document_id}',
    '{var['name']}',
    '{var['display_name']}',
    '{var.get('display_name_kz', '')}',
    '{var.get('description', '')}',
    '{var.get('table', '')}',
    '{var.get('field', '')}',
    '{var['data_type']}',
    {str(var['required']).upper()},
    '{var.get('example', '')}',
    '{var.get('category', '')}'
);
"""
    
    with open(output_path, 'w', encoding=ENCODING_UTF8) as f:
        f.write(sql)
    
    print(f"✅ SQL: {output_path}")
    return output_path


def save_mapping_excel(variables, output_dir):
    output_path = output_dir / "ddu_mapping_template.csv"
    
    import csv
    
    with open(output_path, 'w', encoding=ENCODING_UTF8_SIG, newline='') as f:
        writer = csv.writer(f, delimiter=';')
        
        writer.writerow([
            'ID', 'Имя переменной', 'Отображаемое имя (РУ)', 
            'Отображаемое имя (КЗ)', 'Категория', 'Таблица БД', 
            'Поле БД', 'Тип данных', 'Обязательное', 'Пример значения'
        ])
        
        for var in variables:
            writer.writerow([
                var['id'],
                var['name'],
                var['display_name'],
                var.get('display_name_kz', ''),
                var.get('category', ''),
                var.get('table', ''),
                var.get('field', ''),
                var['data_type'],
                'Да' if var['required'] else 'Нет',
                var.get('example', '')
            ])
    
    print(f"✅ CSV: {output_path}")
    return output_path


def create_api_endpoint_example(variables, output_dir):
    output_path = output_dir / "ddu_api_endpoint_example.py"
    
    code = '''"""
Пример FastAPI endpoint для работы с переменными ДДУ
"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict
from uuid import UUID
from app.models.document import DocumentVariable

router = APIRouter()

DDU_VARIABLES = {
'''
    
    for var in variables:
        code += f'''    "{var['name']}": {{
        "id": "{var['id']}",
        "display_name": "{var['display_name']}",
        "table": "{var.get('table', '')}",
        "field": "{var.get('field', '')}",
    }},
'''
    
    code += '''}

@router.get("/ddu/variables")
async def get_ddu_variables():
    return {"variables": list(DDU_VARIABLES.values())}

@router.post("/ddu/fill")
async def fill_ddu_document(contract_id: str):
    
    filled_variables = {}
    for var_name, var_info in DDU_VARIABLES.items():
        value = get_from_database(var_info['table'], var_info['field'], contract_id)
        filled_variables[var_info['id']] = value
    
    return {"variables": filled_variables}
'''
    
    with open(output_path, 'w', encoding=ENCODING_UTF8) as f:
        f.write(code)
    
    print(f"✅ API Example: {output_path}")


def main():
    print("=" * 70)
    print("🏗️  СОЗДАНИЕ БАЗЫ ПЕРЕМЕННЫХ ДЛЯ ДДУ ШЫМКЕНТ")
    print("=" * 70)
    print()
    
    output_dir = Path("variables_export")
    output_dir.mkdir(exist_ok=True)
    
    document_id, document_name, variables = create_ddu_variables()
    
    print(f"📋 Создано переменных: {len(variables)}")
    print()
    
    categories = {}
    for var in variables:
        category = var.get('category', 'Без категории')
        if category not in categories:
            categories[category] = []
        categories[category].append(var)
    
    print("📊 Переменные по категориям:")
    print("-" * 70)
    for category, vars_list in sorted(categories.items()):
        print(f"  {category:30s} - {len(vars_list):2d} переменных")
    print()
    
    print("💾 Сохранение...")
    print()
    
    save_to_json(document_id, document_name, variables, output_dir)
    save_to_sql(document_id, document_name, variables, output_dir)
    save_mapping_excel(variables, output_dir)
    create_api_endpoint_example(variables, output_dir)
    
    print()
    print("=" * 70)
    print("✅ ГОТОВО!")
    print("=" * 70)
    print()
    print(f"📁 Все файлы в: {output_dir.absolute()}")
    print()
    print("📝 Созданные файлы:")
    print("   1. ddu_variables.json - Полная база переменных")
    print("   2. ddu_variables.sql - SQL скрипт для БД")
    print("   3. ddu_mapping_template.csv - Таблица для Excel")
    print("   4. ddu_api_endpoint_example.py - Пример API")
    print()
    print("📚 Следующие шаги:")
    print("   1. Откройте ddu_mapping_template.csv в Excel")
    print("   2. Проверьте соответствие полей вашей БД")
    print("   3. Выполните ddu_variables.sql в БД")
    print("   4. Интегрируйте API endpoint в ваш backend")
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

