-- Добавление тестовых документов для демо-режима
-- Этот скрипт создаёт примеры договоров ДДУ

-- Очистка существующих данных (если есть)
TRUNCATE TABLE document_variables, documents CASCADE;

-- Добавление тестовых документов
INSERT INTO documents (id, name, file_name, created_at) VALUES
  ('550e8400-e29b-41d4-a716-446655440001', 'Договор ДДУ Шымкент - Шаблон №1', 'ДДУ_Шымкент_Шаблон1.docx', CURRENT_TIMESTAMP),
  ('550e8400-e29b-41d4-a716-446655440002', 'Договор ДДУ Шымкент - Шаблон №2', 'ДДУ_Шымкент_Шаблон2.docx', CURRENT_TIMESTAMP),
  ('550e8400-e29b-41d4-a716-446655440003', 'Договор ДДУ Астана - Шаблон', 'ДДУ_Астана_Шаблон.docx', CURRENT_TIMESTAMP),
  ('550e8400-e29b-41d4-a716-446655440004', 'Договор ДДУ Алматы - Шаблон', 'ДДУ_Алматы_Шаблон.docx', CURRENT_TIMESTAMP);

-- Добавление переменных для первого документа
INSERT INTO document_variables (id, document_id, variable_name, variable_type, description, default_value, is_required, created_at) VALUES
  ('650e8400-e29b-41d4-a716-446655440001', '550e8400-e29b-41d4-a716-446655440001', 'contract_number', 'string', 'Номер договора', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440002', '550e8400-e29b-41d4-a716-446655440001', 'contract_date', 'date', 'Дата договора', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440003', '550e8400-e29b-41d4-a716-446655440001', 'seller_name', 'string', 'Наименование продавца', 'ТОО "БИ Строй"', true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440004', '550e8400-e29b-41d4-a716-446655440001', 'buyer_name', 'string', 'ФИО покупателя', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440005', '550e8400-e29b-41d4-a716-446655440001', 'buyer_iin', 'string', 'ИИН покупателя', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440006', '550e8400-e29b-41d4-a716-446655440001', 'apartment_number', 'string', 'Номер квартиры', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440007', '550e8400-e29b-41d4-a716-446655440001', 'apartment_area', 'number', 'Площадь квартиры (кв.м)', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440008', '550e8400-e29b-41d4-a716-446655440001', 'apartment_price', 'number', 'Стоимость квартиры (тенге)', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440009', '550e8400-e29b-41d4-a716-446655440001', 'building_address', 'string', 'Адрес объекта строительства', 'г. Шымкент, мкр. Нурсат', false, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440010', '550e8400-e29b-41d4-a716-446655440001', 'completion_date', 'date', 'Срок завершения строительства', '2026-12-31', false, CURRENT_TIMESTAMP);

-- Добавление переменных для второго документа
INSERT INTO document_variables (id, document_id, variable_name, variable_type, description, default_value, is_required, created_at) VALUES
  ('650e8400-e29b-41d4-a716-446655440011', '550e8400-e29b-41d4-a716-446655440002', 'contract_number', 'string', 'Номер договора', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440012', '550e8400-e29b-41d4-a716-446655440002', 'contract_date', 'date', 'Дата договора', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440013', '550e8400-e29b-41d4-a716-446655440002', 'buyer_name', 'string', 'ФИО покупателя', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440014', '550e8400-e29b-41d4-a716-446655440002', 'apartment_number', 'string', 'Номер квартиры', NULL, true, CURRENT_TIMESTAMP);

-- Добавление переменных для третьего документа  
INSERT INTO document_variables (id, document_id, variable_name, variable_type, description, default_value, is_required, created_at) VALUES
  ('650e8400-e29b-41d4-a716-446655440015', '550e8400-e29b-41d4-a716-446655440003', 'contract_number', 'string', 'Номер договора', NULL, true, CURRENT_TIMESTAMP),
  ('650e8400-e29b-41d4-a716-446655440016', '550e8400-e29b-41d4-a716-446655440003', 'buyer_name', 'string', 'ФИО покупателя', NULL, true, CURRENT_TIMESTAMP);

-- Вывод результата
SELECT 'Добавлено документов: ' || COUNT(*) FROM documents;
SELECT 'Добавлено переменных: ' || COUNT(*) FROM document_variables;

