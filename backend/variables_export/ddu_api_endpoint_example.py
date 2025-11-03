"""
Пример FastAPI endpoint для работы с переменными ДДУ
"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict
from uuid import UUID
from app.models.document import DocumentVariable

router = APIRouter()

# Маппинг переменных (генерируется автоматически)
DDU_VARIABLES = {
    "CONTRACT_NUMBER": {
        "id": "237701d3-4b58-4c45-ba2d-d0cbe407089b",
        "display_name": "Номер договора",
        "table": "contracts",
        "field": "contract_number",
    },
    "CONTRACT_DATE": {
        "id": "40484073-6912-4517-a596-8bd4359bd7b3",
        "display_name": "Дата договора",
        "table": "contracts",
        "field": "contract_date",
    },
    "CONTRACT_PLACE": {
        "id": "acbcf0d4-509a-4e42-af37-f0a700df2385",
        "display_name": "Место заключения договора",
        "table": "contracts",
        "field": "contract_place",
    },
    "CONTRACT_YEAR": {
        "id": "c9e186bf-cd5d-4226-b4fa-eb99954461c3",
        "display_name": "Год договора",
        "table": "contracts",
        "field": "contract_year",
    },
    "COMPANY_NAME": {
        "id": "47f6b62c-6fd6-446a-a774-a8d278ff1731",
        "display_name": "Наименование компании",
        "table": "companies",
        "field": "company_name",
    },
    "COMPANY_DIRECTOR": {
        "id": "ea8eff8f-b7aa-4777-9803-15dfe4a912d9",
        "display_name": "Руководитель компании",
        "table": "companies",
        "field": "director_name",
    },
    "COMPANY_BASIS": {
        "id": "2739e362-e271-4dbc-ad12-784c20f5dc63",
        "display_name": "Основание полномочий",
        "table": "companies",
        "field": "authority_basis",
    },
    "COMPANY_BIN": {
        "id": "74f37c09-554f-4ae5-ad25-37c7bd2df917",
        "display_name": "БИН компании",
        "table": "companies",
        "field": "bin",
    },
    "COMPANY_ADDRESS": {
        "id": "c1b39f73-0e01-4287-ac7b-5d2311fa5610",
        "display_name": "Юридический адрес компании",
        "table": "companies",
        "field": "legal_address",
    },
    "COMPANY_PHONE": {
        "id": "95d939d9-575d-4de6-852c-c168a4ad7818",
        "display_name": "Телефон компании",
        "table": "companies",
        "field": "phone",
    },
    "COMPANY_EMAIL": {
        "id": "b31b3e2d-d052-4a23-82e3-c1c979e74afa",
        "display_name": "Email компании",
        "table": "companies",
        "field": "email",
    },
    "COMPANY_BANK": {
        "id": "e0344aff-4606-4395-954a-fc1f2850a450",
        "display_name": "Банк компании",
        "table": "companies",
        "field": "bank_name",
    },
    "COMPANY_ACCOUNT": {
        "id": "06b83b4c-bdcd-4047-adb8-bfa43ab53155",
        "display_name": "Расчетный счет",
        "table": "companies",
        "field": "account_number",
    },
    "COMPANY_BIK": {
        "id": "37c3395f-b3ed-4944-8105-9e6fe83ec04b",
        "display_name": "БИК банка",
        "table": "companies",
        "field": "bik",
    },
    "CLIENT_FIO": {
        "id": "6a1b9b29-680a-4fa5-94c7-12afb6da513c",
        "display_name": "ФИО дольщика",
        "table": "clients",
        "field": "full_name",
    },
    "CLIENT_IIN": {
        "id": "f86b04e4-5d0d-42d8-8a00-fb3ecef99e76",
        "display_name": "ИИН дольщика",
        "table": "clients",
        "field": "iin",
    },
    "CLIENT_ADDRESS": {
        "id": "0b0968bb-26fc-4223-adb2-4203a543d337",
        "display_name": "Адрес дольщика",
        "table": "clients",
        "field": "address",
    },
    "CLIENT_PHONE": {
        "id": "98bdfd0d-086a-469a-8b37-ba70965aaed3",
        "display_name": "Телефон дольщика",
        "table": "clients",
        "field": "phone",
    },
    "CLIENT_EMAIL": {
        "id": "976c48b7-aa10-4627-a802-d0874e5e2130",
        "display_name": "Email дольщика",
        "table": "clients",
        "field": "email",
    },
    "CLIENT_PASSPORT": {
        "id": "243ac31e-b682-4f5a-af04-cf53877382a0",
        "display_name": "Документ удостоверяющий личность",
        "table": "clients",
        "field": "passport_number",
    },
    "CLIENT_PASSPORT_ISSUED_BY": {
        "id": "3fde5412-cc8b-45ea-a774-f8e0006fe066",
        "display_name": "Кем выдан документ",
        "table": "clients",
        "field": "passport_issued_by",
    },
    "CLIENT_PASSPORT_DATE": {
        "id": "ad608c2d-b622-41c4-b6fe-1da063414e5d",
        "display_name": "Дата выдачи документа",
        "table": "clients",
        "field": "passport_issue_date",
    },
    "APARTMENT_NUMBER": {
        "id": "a2adfbff-c4c2-4bca-a90c-283d57676d1b",
        "display_name": "Номер квартиры",
        "table": "apartments",
        "field": "apartment_number",
    },
    "APARTMENT_FLOOR": {
        "id": "b8a92a32-4663-4285-bcb9-3fd8410bb9a9",
        "display_name": "Этаж",
        "table": "apartments",
        "field": "floor",
    },
    "APARTMENT_AREA": {
        "id": "85e9526e-1938-4fc6-9f5f-1c24c1dd13b3",
        "display_name": "Общая площадь",
        "table": "apartments",
        "field": "total_area",
    },
    "APARTMENT_ROOMS": {
        "id": "8866e4a9-50c1-455c-af05-632ff2f5fad2",
        "display_name": "Количество комнат",
        "table": "apartments",
        "field": "rooms_count",
    },
    "BUILDING_ADDRESS": {
        "id": "c7f8e748-3549-4338-b1e8-59bedc67c454",
        "display_name": "Адрес дома",
        "table": "buildings",
        "field": "address",
    },
    "BUILDING_CADASTRAL": {
        "id": "33e40fc2-0a3d-4d1d-861d-6e32acc9841e",
        "display_name": "Кадастровый номер",
        "table": "buildings",
        "field": "cadastral_number",
    },
    "PRICE_TOTAL": {
        "id": "8266acb7-69e0-4199-a2ba-70f8cdb093ac",
        "display_name": "Стоимость доли",
        "table": "contracts",
        "field": "price_total",
    },
    "PRICE_PER_METER": {
        "id": "2debe0f6-5086-48e8-85ca-b7819d3428d4",
        "display_name": "Цена за кв.м",
        "table": "contracts",
        "field": "price_per_meter",
    },
    "PAYMENT_SCHEDULE": {
        "id": "4bb3f784-a5b1-496f-8978-cd7a8c37b8db",
        "display_name": "График платежей",
        "table": "contracts",
        "field": "payment_schedule",
    },
    "COMPLETION_DATE": {
        "id": "1411c76c-38a9-45a8-8be7-05d68a4aa524",
        "display_name": "Срок сдачи дома",
        "table": "contracts",
        "field": "completion_date",
    },
    "ACCEPTANCE_ACT_NUMBER": {
        "id": "068f3184-d24f-46f2-a736-6fb9845845af",
        "display_name": "Номер акта приемки",
        "table": "documents",
        "field": "acceptance_act_number",
    },
    "ACCEPTANCE_ACT_DATE": {
        "id": "a83d742c-b7c1-413c-8340-979762b1ef3b",
        "display_name": "Дата акта приемки",
        "table": "documents",
        "field": "acceptance_act_date",
    },
    "REGISTRATION_NUMBER": {
        "id": "ecd72d8d-6c96-47d3-b827-6cb3437ae4c7",
        "display_name": "Номер регистрации",
        "table": "documents",
        "field": "registration_number",
    },
    "REGISTRATION_DATE": {
        "id": "96b09609-2221-4439-84df-819f74f46d00",
        "display_name": "Дата регистрации",
        "table": "documents",
        "field": "registration_date",
    },
    "KEYS_COUNT": {
        "id": "e6f9652f-decc-4b07-9c3a-b11ff9aa1699",
        "display_name": "Количество ключей",
        "table": "contracts",
        "field": "keys_count",
    },
    "WITNESS_NAME": {
        "id": "6bbf1b9c-3d89-4482-8f0c-ff2e48492c7a",
        "display_name": "ФИО свидетеля",
        "table": "contracts",
        "field": "witness_name",
    },
}

@router.get("/ddu/variables")
async def get_ddu_variables():
    """Получить все переменные для ДДУ"""
    return {"variables": list(DDU_VARIABLES.values())}

@router.post("/ddu/fill")
async def fill_ddu_document(contract_id: str):
    """Заполнить документ ДДУ данными из БД"""
    # TODO: Получить данные из БД по contract_id
    # TODO: Заполнить переменные
    # TODO: Вернуть заполненный документ
    
    filled_variables = {}
    for var_name, var_info in DDU_VARIABLES.items():
        # Здесь запрос в БД
        value = get_from_database(var_info['table'], var_info['field'], contract_id)
        filled_variables[var_info['id']] = value
    
    return {"variables": filled_variables}
