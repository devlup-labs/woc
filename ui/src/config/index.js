export const USE_HTTPS = process.env.NODE_ENV === 'production'
export const BACKEND_API_HOST = '127.0.0.1'
export const BACKEND_API_PORT = 8000
export const BACKEND_API_ADDRESS = (USE_HTTPS ? 'https://' : 'http://') + BACKEND_API_HOST + (USE_HTTPS ? '' : ':' + BACKEND_API_PORT)
