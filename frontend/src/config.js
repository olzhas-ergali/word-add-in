const CONFIG = {
    /**
     * В Docker надстройка открывается с https://localhost:3000 — API должен идти с того же origin
     * (прокси /api/ в nginx), иначе браузер/WebView блокирует mixed content (HTTPS → http://8000).
     * Прямой backend: http://localhost:8000 — только при локальном запуске без nginx.
     */
    get API_BASE_URL() {
        if (typeof window !== 'undefined' && window.location) {
            const h = window.location.hostname;
            const p = window.location.port;
            if (h === 'localhost' && (p === '3000' || p === '3001')) {
                return window.location.origin;
            }
        }
        return 'http://localhost:8000';
    },
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

