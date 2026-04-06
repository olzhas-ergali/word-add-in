class ApiService {
    constructor() {
        this.baseUrl = CONFIG.API_BASE_URL;
        this.sessionId = localStorage.getItem(CONFIG.STORAGE_KEYS.SESSION_ID);
        
        if (!this.sessionId) {
            this.sessionId = 'demo-auto-session-' + Date.now();
            localStorage.setItem(CONFIG.STORAGE_KEYS.SESSION_ID, this.sessionId);
            localStorage.setItem(CONFIG.STORAGE_KEYS.ACCESS_TOKEN, 'demo-token');
        }
    }

    getHeaders() {
        const headers = {'Content-Type': 'application/json'};
        if (this.sessionId) {
            headers['X-Session-ID'] = this.sessionId;
        }
        return headers;
    }

    async request(path, options = {}) {
        try {
            const response = await fetch(`${this.baseUrl}${path}`, options);
            return response;
        } catch (error) {
            const message = String(error?.message || error || "");
            const sslLikely = message.includes("Failed to fetch") || message.includes("NetworkError");
            if (sslLikely) {
                throw new Error(
                    "Не удалось установить защищенное соединение с сервисом. " +
                    "Проверьте, что сертификат localhost доверен в Windows, затем перезапустите Word."
                );
            }
            throw error;
        }
    }

    async login(username, password) {
        try {
            const response = await this.request(`${CONFIG.ENDPOINTS.LOGIN}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail?.message || data.message || 'Login failed');
            }
            if (data.session_id) {
                this.sessionId = data.session_id;
                localStorage.setItem(CONFIG.STORAGE_KEYS.SESSION_ID, data.session_id);
            }
            if (data.data?.access_token) {
                localStorage.setItem(CONFIG.STORAGE_KEYS.ACCESS_TOKEN, data.data.access_token);
            }
            return data;
        } catch (error) {
            console.error('Login error:', error);
            throw error;
        }
    }

    async logout() {
        try {
            await this.request(`${CONFIG.ENDPOINTS.LOGOUT}`, {
                method: 'POST',
                headers: this.getHeaders()
            });
            localStorage.removeItem(CONFIG.STORAGE_KEYS.SESSION_ID);
            localStorage.removeItem(CONFIG.STORAGE_KEYS.ACCESS_TOKEN);
            localStorage.removeItem(CONFIG.STORAGE_KEYS.SELECTED_DOCUMENT);
            this.sessionId = null;
        } catch (error) {
            console.error('Logout error:', error);
        }
    }

    async getDocuments() {
        try {
            const response = await this.request(`${CONFIG.ENDPOINTS.DOCUMENTS}`, {
                method: 'GET',
                headers: this.getHeaders()
            });
            if (!response.ok) {
                throw new Error('Failed to fetch documents');
            }
            return await response.json();
        } catch (error) {
            console.error('Get documents error:', error);
            throw error;
        }
    }

    async downloadDocument(documentId) {
        try {
            const response = await this.request(
                `${CONFIG.ENDPOINTS.DOWNLOAD}/${documentId}`,
                {method: 'GET', headers: this.getHeaders()}
            );
            if (!response.ok) {
                throw new Error('Failed to download document');
            }
            return await response.blob();
        } catch (error) {
            console.error('Download document error:', error);
            throw error;
        }
    }

    async getDocumentVariables(documentId) {
        try {
            const response = await this.request(
                `${CONFIG.ENDPOINTS.VARIABLES}/${documentId}`,
                {method: 'GET', headers: this.getHeaders()}
            );
            if (!response.ok) {
                throw new Error('Failed to fetch document variables');
            }
            return await response.json();
        } catch (error) {
            console.error('Get document variables error:', error);
            throw error;
        }
    }

    async getVariableValues(variableIds) {
        try {
            const response = await this.request(
                `${CONFIG.ENDPOINTS.VARIABLE_VALUES}`,
                {
                    method: 'POST',
                    headers: this.getHeaders(),
                    body: JSON.stringify({ ids: variableIds })
                }
            );
            if (!response.ok) {
                throw new Error('Failed to fetch variable values');
            }
            return await response.json();
        } catch (error) {
            console.error('Get variable values error:', error);
            throw error;
        }
    }

    isAuthenticated() {
        this.sessionId = localStorage.getItem(CONFIG.STORAGE_KEYS.SESSION_ID);
        return !!this.sessionId;
    }
    
    getSessionId() {
        return this.sessionId || localStorage.getItem(CONFIG.STORAGE_KEYS.SESSION_ID);
    }
}

const apiService = new ApiService();

