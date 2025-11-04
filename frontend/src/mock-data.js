/**
 * Mock данные для работы без Backend
 * Используется когда backend недоступен
 */

const MOCK_DATA = {
    // Тестовые параметры
    parameters: [
        {
            id: 1,
            contract_id: "DDU-2024-001",
            param_name: "CLIENT_FIO",
            param_value: "Иванов Иван Иванович",
            description: "ФИО дольщика",
            created_at: new Date().toISOString()
        },
        {
            id: 2,
            contract_id: "DDU-2024-001",
            param_name: "CONTRACT_NUMBER",
            param_value: "ADL-1-204/41",
            description: "Номер договора",
            created_at: new Date().toISOString()
        },
        {
            id: 3,
            contract_id: "DDU-2024-001",
            param_name: "CONTRACT_DATE",
            param_value: "25.02.2024",
            description: "Дата договора",
            created_at: new Date().toISOString()
        },
        {
            id: 4,
            contract_id: "DDU-2024-001",
            param_name: "APARTMENT_NUMBER",
            param_value: "204",
            description: "Номер квартиры",
            created_at: new Date().toISOString()
        },
        {
            id: 5,
            contract_id: "DDU-2024-001",
            param_name: "APARTMENT_AREA",
            param_value: "65.5",
            description: "Площадь квартиры",
            created_at: new Date().toISOString()
        },
        {
            id: 6,
            contract_id: "DDU-2024-001",
            param_name: "PRICE_TOTAL",
            param_value: "15000000",
            description: "Стоимость",
            created_at: new Date().toISOString()
        },
        {
            id: 7,
            contract_id: "DDU-2024-002",
            param_name: "CLIENT_FIO",
            param_value: "Петров Петр Петрович",
            description: "ФИО дольщика",
            created_at: new Date().toISOString()
        },
        {
            id: 8,
            contract_id: "DDU-2024-002",
            param_name: "CONTRACT_NUMBER",
            param_value: "ADL-1-205/42",
            description: "Номер договора",
            created_at: new Date().toISOString()
        }
    ],
    
    // Тестовые документы
    documents: [
        {
            documentId: "00000000-0000-0000-0000-000000000001",
            fileName: "ДДУ Шаблон.docx",
            contentType: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            createdAt: "2024-01-01T00:00:00Z",
            organizationName: "Демо организация"
        },
        {
            documentId: "00000000-0000-0000-0000-000000000002",
            fileName: "Договор купли-продажи.docx",
            contentType: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            createdAt: "2024-01-02T00:00:00Z",
            organizationName: "Демо организация"
        }
    ]
};

/**
 * Mock API сервис для работы без backend
 */
class MockApiService {
    constructor() {
        this.mode = 'offline';
        this.parameters = [...MOCK_DATA.parameters];
        this.nextId = 9;
    }

    /**
     * Получить все параметры
     */
    async getParameters() {
        await this.delay(300);
        return {
            count: this.parameters.length,
            parameters: this.parameters
        };
    }

    /**
     * Получить параметры по contract_id
     */
    async getParametersByContract(contractId) {
        await this.delay(200);
        const filtered = this.parameters.filter(p => p.contract_id === contractId);
        return {
            contract_id: contractId,
            count: filtered.length,
            parameters: filtered
        };
    }

    /**
     * Добавить параметр
     */
    async addParameter(param) {
        await this.delay(200);
        const newParam = {
            id: this.nextId++,
            contract_id: param.contract_id,
            param_name: param.param_name,
            param_value: param.param_value,
            description: param.description || '',
            created_at: new Date().toISOString(),
            updated_at: new Date().toISOString()
        };
        this.parameters.push(newParam);
        return {
            success: true,
            message: "Параметр добавлен (в памяти, не сохранен)",
            parameter: newParam
        };
    }

    /**
     * Обновить параметр
     */
    async updateParameter(paramId, param) {
        await this.delay(200);
        const index = this.parameters.findIndex(p => p.id === paramId);
        if (index === -1) {
            throw new Error("Параметр не найден");
        }
        
        this.parameters[index] = {
            ...this.parameters[index],
            param_name: param.param_name,
            param_value: param.param_value,
            description: param.description,
            updated_at: new Date().toISOString()
        };
        
        return {
            success: true,
            message: "Параметр обновлен (в памяти)",
            parameter: this.parameters[index]
        };
    }

    /**
     * Удалить параметр
     */
    async deleteParameter(paramId) {
        await this.delay(200);
        const index = this.parameters.findIndex(p => p.id === paramId);
        if (index === -1) {
            throw new Error("Параметр не найден");
        }
        
        this.parameters.splice(index, 1);
        return {
            success: true,
            message: "Параметр удален (из памяти)",
            deleted_id: paramId
        };
    }

    /**
     * Поиск параметров
     */
    async searchParameters(contractId, paramName, paramValue) {
        await this.delay(300);
        let filtered = [...this.parameters];
        
        if (contractId) {
            filtered = filtered.filter(p => 
                p.contract_id.toLowerCase().includes(contractId.toLowerCase())
            );
        }
        if (paramName) {
            filtered = filtered.filter(p => 
                p.param_name.toLowerCase().includes(paramName.toLowerCase())
            );
        }
        if (paramValue) {
            filtered = filtered.filter(p => 
                p.param_value.toLowerCase().includes(paramValue.toLowerCase())
            );
        }
        
        return {
            count: filtered.length,
            parameters: filtered
        };
    }

    /**
     * Получить документы
     */
    async getDocuments() {
        await this.delay(500);
        return MOCK_DATA.documents;
    }

    /**
     * Имитация задержки сети
     */
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Глобальный экземпляр
const mockApiService = new MockApiService();

