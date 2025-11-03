-- SQL скрипт для документа ДДУ Шымкент
-- Дата создания: 2025-11-03 20:41:51
-- Переменных: 38

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
VALUES ('4b746c88-6c86-48b9-afaa-993e883ed7c5', 'ДДУ Шымкент', 'ДДУ Шымкент.docx', NOW())
ON DUPLICATE KEY UPDATE name = 'ДДУ Шымкент';

-- Вставка переменных

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '237701d3-4b58-4c45-ba2d-d0cbe407089b',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CONTRACT_NUMBER',
    'Номер договора',
    'Шарт нөмірі',
    'Номер договора долевого участия',
    'contracts',
    'contract_number',
    'string',
    TRUE,
    'ADL-1-204/41',
    'Договор'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '40484073-6912-4517-a596-8bd4359bd7b3',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CONTRACT_DATE',
    'Дата договора',
    'Шарт күні',
    'Дата заключения договора',
    'contracts',
    'contract_date',
    'date',
    TRUE,
    '25.02.2020',
    'Договор'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'acbcf0d4-509a-4e42-af37-f0a700df2385',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CONTRACT_PLACE',
    'Место заключения договора',
    'Шарт жасасу орны',
    'Город/место заключения договора',
    'contracts',
    'contract_place',
    'string',
    TRUE,
    'г. Нур-Султан',
    'Договор'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'c9e186bf-cd5d-4226-b4fa-eb99954461c3',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CONTRACT_YEAR',
    'Год договора',
    'Шарт жылы',
    'Год заключения договора',
    'contracts',
    'contract_year',
    'number',
    TRUE,
    '2020',
    'Договор'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '47f6b62c-6fd6-446a-a774-a8d278ff1731',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_NAME',
    'Наименование компании',
    'Компания атауы',
    'Полное наименование уполномоченной компании',
    'companies',
    'company_name',
    'string',
    TRUE,
    'ТОО 'Town House'',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'ea8eff8f-b7aa-4777-9803-15dfe4a912d9',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_DIRECTOR',
    'Руководитель компании',
    'Компания басшысы',
    'ФИО руководителя компании',
    'companies',
    'director_name',
    'string',
    TRUE,
    'Иванов Иван Иванович',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '2739e362-e271-4dbc-ad12-784c20f5dc63',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_BASIS',
    'Основание полномочий',
    'Өкілеттік негізі',
    'Документ, на основании которого действует руководитель',
    'companies',
    'authority_basis',
    'string',
    TRUE,
    'Устава',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '74f37c09-554f-4ae5-ad25-37c7bd2df917',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_BIN',
    'БИН компании',
    'Компанияның БСН',
    'Бизнес-идентификационный номер',
    'companies',
    'bin',
    'string',
    TRUE,
    '123456789012',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'c1b39f73-0e01-4287-ac7b-5d2311fa5610',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_ADDRESS',
    'Юридический адрес компании',
    'Компанияның заңды мекенжайы',
    'Полный юридический адрес',
    'companies',
    'legal_address',
    'string',
    TRUE,
    'г. Нур-Султан, ул. Абая, д. 10',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '95d939d9-575d-4de6-852c-c168a4ad7818',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_PHONE',
    'Телефон компании',
    'Компания телефоны',
    'Контактный телефон',
    'companies',
    'phone',
    'string',
    TRUE,
    '+7 (7172) 123-456',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'b31b3e2d-d052-4a23-82e3-c1c979e74afa',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_EMAIL',
    'Email компании',
    'Компания email',
    'Электронная почта',
    'companies',
    'email',
    'string',
    FALSE,
    'info@townhouse.kz',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'e0344aff-4606-4395-954a-fc1f2850a450',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_BANK',
    'Банк компании',
    'Компания банкі',
    'Наименование банка',
    'companies',
    'bank_name',
    'string',
    TRUE,
    'АО 'Народный Банк Казахстана'',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '06b83b4c-bdcd-4047-adb8-bfa43ab53155',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_ACCOUNT',
    'Расчетный счет',
    'Есеп шоты',
    'Номер расчетного счета',
    'companies',
    'account_number',
    'string',
    TRUE,
    'KZ123456789012345678',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '37c3395f-b3ed-4944-8105-9e6fe83ec04b',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPANY_BIK',
    'БИК банка',
    'Банктің БСК',
    'БИК банка компании',
    'companies',
    'bik',
    'string',
    TRUE,
    'HSBKKZKX',
    'Уполномоченная компания'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '6a1b9b29-680a-4fa5-94c7-12afb6da513c',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_FIO',
    'ФИО дольщика',
    'Үлескердің Т.А.Ә.',
    'Полное имя дольщика',
    'clients',
    'full_name',
    'string',
    TRUE,
    'Петров Петр Петрович',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'f86b04e4-5d0d-42d8-8a00-fb3ecef99e76',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_IIN',
    'ИИН дольщика',
    'Үлескердің ЖСН',
    'Индивидуальный идентификационный номер',
    'clients',
    'iin',
    'string',
    TRUE,
    '900101300123',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '0b0968bb-26fc-4223-adb2-4203a543d337',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_ADDRESS',
    'Адрес дольщика',
    'Үлескердің мекенжайы',
    'Адрес регистрации дольщика',
    'clients',
    'address',
    'string',
    TRUE,
    'г. Нур-Султан, ул. Кенесары, д. 5, кв. 10',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '98bdfd0d-086a-469a-8b37-ba70965aaed3',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_PHONE',
    'Телефон дольщика',
    'Үлескердің телефоны',
    'Контактный телефон дольщика',
    'clients',
    'phone',
    'string',
    TRUE,
    '+7 (777) 123-45-67',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '976c48b7-aa10-4627-a802-d0874e5e2130',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_EMAIL',
    'Email дольщика',
    'Үлескердің email',
    'Электронная почта дольщика',
    'clients',
    'email',
    'string',
    FALSE,
    'petrov@mail.ru',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '243ac31e-b682-4f5a-af04-cf53877382a0',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_PASSPORT',
    'Документ удостоверяющий личность',
    'Жеке куәлік',
    'Серия и номер документа',
    'clients',
    'passport_number',
    'string',
    TRUE,
    'N 12345678',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '3fde5412-cc8b-45ea-a774-f8e0006fe066',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_PASSPORT_ISSUED_BY',
    'Кем выдан документ',
    'Құжатты кім берген',
    'Орган, выдавший документ',
    'clients',
    'passport_issued_by',
    'string',
    TRUE,
    'МВД РК',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'ad608c2d-b622-41c4-b6fe-1da063414e5d',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'CLIENT_PASSPORT_DATE',
    'Дата выдачи документа',
    'Құжат берілген күні',
    'Дата выдачи документа',
    'clients',
    'passport_issue_date',
    'date',
    TRUE,
    '01.01.2020',
    'Дольщик'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'a2adfbff-c4c2-4bca-a90c-283d57676d1b',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'APARTMENT_NUMBER',
    'Номер квартиры',
    'Пәтер нөмірі',
    'Номер квартиры в доме',
    'apartments',
    'apartment_number',
    'string',
    TRUE,
    '204',
    'Объект'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'b8a92a32-4663-4285-bcb9-3fd8410bb9a9',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'APARTMENT_FLOOR',
    'Этаж',
    'Қабат',
    'Этаж расположения квартиры',
    'apartments',
    'floor',
    'number',
    TRUE,
    '5',
    'Объект'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '85e9526e-1938-4fc6-9f5f-1c24c1dd13b3',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'APARTMENT_AREA',
    'Общая площадь',
    'Жалпы алаң',
    'Общая площадь квартиры в кв.м',
    'apartments',
    'total_area',
    'number',
    TRUE,
    '65.5',
    'Объект'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '8866e4a9-50c1-455c-af05-632ff2f5fad2',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'APARTMENT_ROOMS',
    'Количество комнат',
    'Бөлмелер саны',
    'Количество жилых комнат',
    'apartments',
    'rooms_count',
    'number',
    TRUE,
    '2',
    'Объект'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'c7f8e748-3549-4338-b1e8-59bedc67c454',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'BUILDING_ADDRESS',
    'Адрес дома',
    'Үйдің мекенжайы',
    'Полный адрес многоквартирного дома',
    'buildings',
    'address',
    'string',
    TRUE,
    'г. Шымкент, мкр. Нурсат, ул. Жантокова, д. 1',
    'Объект'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '33e40fc2-0a3d-4d1d-861d-6e32acc9841e',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'BUILDING_CADASTRAL',
    'Кадастровый номер',
    'Кадастрлық нөмір',
    'Кадастровый номер здания',
    'buildings',
    'cadastral_number',
    'string',
    FALSE,
    '10-111-222-333',
    'Объект'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '8266acb7-69e0-4199-a2ba-70f8cdb093ac',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'PRICE_TOTAL',
    'Стоимость доли',
    'Үлестің құны',
    'Полная стоимость доли',
    'contracts',
    'price_total',
    'number',
    TRUE,
    '15000000',
    'Финансы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '2debe0f6-5086-48e8-85ca-b7819d3428d4',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'PRICE_PER_METER',
    'Цена за кв.м',
    'Шаршы метрдің бағасы',
    'Стоимость одного квадратного метра',
    'contracts',
    'price_per_meter',
    'number',
    TRUE,
    '228000',
    'Финансы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '4bb3f784-a5b1-496f-8978-cd7a8c37b8db',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'PAYMENT_SCHEDULE',
    'График платежей',
    'Төлем кестесі',
    'График платежей',
    'contracts',
    'payment_schedule',
    'text',
    FALSE,
    'Согласно приложению №3',
    'Финансы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '1411c76c-38a9-45a8-8be7-05d68a4aa524',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'COMPLETION_DATE',
    'Срок сдачи дома',
    'Үйді тапсыру мерзімі',
    'Планируемая дата сдачи дома',
    'contracts',
    'completion_date',
    'date',
    TRUE,
    '31.12.2024',
    'Сроки'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '068f3184-d24f-46f2-a736-6fb9845845af',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'ACCEPTANCE_ACT_NUMBER',
    'Номер акта приемки',
    'Қабылдау актісінің нөмірі',
    'Номер акта приемки в эксплуатацию',
    'documents',
    'acceptance_act_number',
    'string',
    FALSE,
    'АКТ-2024-001',
    'Документы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'a83d742c-b7c1-413c-8340-979762b1ef3b',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'ACCEPTANCE_ACT_DATE',
    'Дата акта приемки',
    'Қабылдау актісінің күні',
    'Дата акта приемки в эксплуатацию',
    'documents',
    'acceptance_act_date',
    'date',
    FALSE,
    '15.12.2024',
    'Документы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'ecd72d8d-6c96-47d3-b827-6cb3437ae4c7',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'REGISTRATION_NUMBER',
    'Номер регистрации',
    'Тіркеу нөмірі',
    'Номер государственной регистрации',
    'documents',
    'registration_number',
    'string',
    FALSE,
    'РЕГ-2024-12345',
    'Документы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '96b09609-2221-4439-84df-819f74f46d00',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'REGISTRATION_DATE',
    'Дата регистрации',
    'Тіркеу күні',
    'Дата государственной регистрации',
    'documents',
    'registration_date',
    'date',
    FALSE,
    '20.12.2024',
    'Документы'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    'e6f9652f-decc-4b07-9c3a-b11ff9aa1699',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'KEYS_COUNT',
    'Количество ключей',
    'Кілттер саны',
    'Количество переданных ключей',
    'contracts',
    'keys_count',
    'number',
    TRUE,
    '2',
    'Дополнительно'
);

INSERT INTO document_variables (
    id, document_id, name, display_name, display_name_kz, description,
    table_name, field_name, data_type, required, example, category
) VALUES (
    '6bbf1b9c-3d89-4482-8f0c-ff2e48492c7a',
    '4b746c88-6c86-48b9-afaa-993e883ed7c5',
    'WITNESS_NAME',
    'ФИО свидетеля',
    'Куәгердің Т.А.Ә.',
    'ФИО свидетеля сделки',
    'contracts',
    'witness_name',
    'string',
    FALSE,
    'Сидоров Сергей Сергеевич',
    'Дополнительно'
);
