/**
 * API service for communicating with backend
 */
class ApiService {
    constructor() {
        this.baseUrl = CONFIG.API_BASE_URL;
        this.sessionId = localStorage.getItem(CONFIG.STORAGE_KEYS.SESSION_ID);
    }

    /**
     * Get headers with session ID
     */
    getHeaders() {
        const headers = {
            'Content-Type': 'application/json'
        };
        
        if (this.sessionId) {
            headers['X-Session-ID'] = this.sessionId;
        }
        
        return headers;
    }

    /**
     * Login user
     */
    async login(username, password) {
        try {
            const response = await fetch(`${this.baseUrl}${CONFIG.ENDPOINTS.LOGIN}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail?.message || data.message || 'Login failed');
            }

            // Save session ID
            if (data.session_id) {
                this.sessionId = data.session_id;
                localStorage.setItem(CONFIG.STORAGE_KEYS.SESSION_ID, data.session_id);
            }

            // Save access token
            if (data.data?.access_token) {
                localStorage.setItem(CONFIG.STORAGE_KEYS.ACCESS_TOKEN, data.data.access_token);
            }

            return data;
        } catch (error) {
            console.error('Login error:', error);
            throw error;
        }
    }

    /**
     * Logout user
     */
    async logout() {
        try {
            await fetch(`${this.baseUrl}${CONFIG.ENDPOINTS.LOGOUT}`, {
                method: 'POST',
                headers: this.getHeaders()
            });

            // Clear local storage
            localStorage.removeItem(CONFIG.STORAGE_KEYS.SESSION_ID);
            localStorage.removeItem(CONFIG.STORAGE_KEYS.ACCESS_TOKEN);
            localStorage.removeItem(CONFIG.STORAGE_KEYS.SELECTED_DOCUMENT);
            this.sessionId = null;
        } catch (error) {
            console.error('Logout error:', error);
        }
    }

    /**
     * Get list of documents
     */
    async getDocuments() {
        try {
            const response = await fetch(`${this.baseUrl}${CONFIG.ENDPOINTS.DOCUMENTS}`, {
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

    /**
     * Download document
     */
    async downloadDocument(documentId) {
        try {
            const response = await fetch(
                `${this.baseUrl}${CONFIG.ENDPOINTS.DOWNLOAD}/${documentId}`,
                {
                    method: 'GET',
                    headers: this.getHeaders()
                }
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

    /**
     * Get document variables
     */
    async getDocumentVariables(documentId) {
        try {
            const response = await fetch(
                `${this.baseUrl}${CONFIG.ENDPOINTS.VARIABLES}/${documentId}`,
                {
                    method: 'GET',
                    headers: this.getHeaders()
                }
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

    /**
     * Get variable values
     */
    async getVariableValues(variableIds) {
        try {
            const response = await fetch(
                `${this.baseUrl}${CONFIG.ENDPOINTS.VARIABLE_VALUES}`,
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

    /**
     * Check if user is authenticated
     */
    isAuthenticated() {
        return !!this.sessionId;
    }
}

// Create global API service instance
const apiService = new ApiService();

