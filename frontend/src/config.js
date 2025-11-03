/**
 * Configuration for the Word Add-in
 */
const CONFIG = {
    // Backend API URL
    API_BASE_URL: 'http://localhost:8000',
    
    // API Endpoints
    ENDPOINTS: {
        LOGIN: '/api/auth/login',
        LOGOUT: '/api/auth/logout',
        VALIDATE: '/api/auth/validate',
        DOCUMENTS: '/api/documents/list',
        DOWNLOAD: '/api/documents/download',
        VARIABLES: '/api/variables/document',
        VARIABLE_VALUES: '/api/variables/values'
    },
    
    // Session storage keys
    STORAGE_KEYS: {
        SESSION_ID: 'pf_session_id',
        ACCESS_TOKEN: 'pf_access_token',
        SELECTED_DOCUMENT: 'pf_selected_document'
    }
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}

