const CONFIG = {
    API_BASE_URL: 'http://localhost:8000',
    ENDPOINTS: {
        LOGIN: '/api/auth/login',
        LOGOUT: '/api/auth/logout',
        VALIDATE: '/api/auth/validate',
        DOCUMENTS: '/api/documents/list',
        DOWNLOAD: '/api/documents/download',
        VARIABLES: '/api/variables/document',
        VARIABLE_VALUES: '/api/variables/values'
    },
    STORAGE_KEYS: {
        SESSION_ID: 'pf_session_id',
        ACCESS_TOKEN: 'pf_access_token',
        SELECTED_DOCUMENT: 'pf_selected_document'
    }
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}

