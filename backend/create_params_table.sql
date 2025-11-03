-- Создание таблицы для хранения параметров договоров
-- Выполните этот SQL скрипт в вашей базе данных

-- PostgreSQL
CREATE TABLE IF NOT EXISTS contract_parameters (
    id SERIAL PRIMARY KEY,
    contract_id VARCHAR(255) NOT NULL,
    param_name VARCHAR(255) NOT NULL,
    param_value TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Индексы для быстрого поиска
    CONSTRAINT unique_contract_param UNIQUE (contract_id, param_name)
);

-- Индексы
CREATE INDEX idx_contract_id ON contract_parameters(contract_id);
CREATE INDEX idx_param_name ON contract_parameters(param_name);
CREATE INDEX idx_created_at ON contract_parameters(created_at DESC);

-- Триггер для обновления updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_contract_parameters_updated_at 
    BEFORE UPDATE ON contract_parameters
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Примеры данных для тестирования
INSERT INTO contract_parameters (contract_id, param_name, param_value, description) VALUES
('DDU-2024-001', 'CLIENT_FIO', 'Иванов Иван Иванович', 'ФИО дольщика'),
('DDU-2024-001', 'CONTRACT_NUMBER', 'ADL-1-204/41', 'Номер договора'),
('DDU-2024-001', 'CONTRACT_DATE', '25.02.2024', 'Дата договора'),
('DDU-2024-001', 'APARTMENT_NUMBER', '204', 'Номер квартиры'),
('DDU-2024-001', 'APARTMENT_AREA', '65.5', 'Площадь квартиры'),
('DDU-2024-001', 'PRICE_TOTAL', '15000000', 'Стоимость'),
('DDU-2024-002', 'CLIENT_FIO', 'Петров Петр Петрович', 'ФИО дольщика'),
('DDU-2024-002', 'CONTRACT_NUMBER', 'ADL-1-205/42', 'Номер договора'),
('DDU-2024-002', 'CONTRACT_DATE', '26.02.2024', 'Дата договора')
ON CONFLICT (contract_id, param_name) DO NOTHING;

COMMENT ON TABLE contract_parameters IS 'Параметры договоров для заполнения Word документов';
COMMENT ON COLUMN contract_parameters.contract_id IS 'ID договора (уникальный идентификатор)';
COMMENT ON COLUMN contract_parameters.param_name IS 'Имя параметра (например, CLIENT_FIO)';
COMMENT ON COLUMN contract_parameters.param_value IS 'Значение параметра';
COMMENT ON COLUMN contract_parameters.description IS 'Описание параметра';

-- Для MySQL (если используете MySQL вместо PostgreSQL):
/*
CREATE TABLE IF NOT EXISTS contract_parameters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contract_id VARCHAR(255) NOT NULL,
    param_name VARCHAR(255) NOT NULL,
    param_value TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    UNIQUE KEY unique_contract_param (contract_id, param_name),
    INDEX idx_contract_id (contract_id),
    INDEX idx_param_name (param_name),
    INDEX idx_created_at (created_at DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
*/

