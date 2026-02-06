import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para manejar errores
apiClient.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

export default {
  // Validar datos sin guardar
  validarDatos(tipoRegistro, datos) {
    return apiClient.post('/validar/', {
      tipo_registro: tipoRegistro,
      datos: datos
    })
  },
  
  // Crear preregistro
  crearPreregistro(tipoRegistro, datos) {
    return apiClient.post('/preregistro/', {
      tipo_registro: tipoRegistro,
      datos: datos
    })
  },
  
  // Obtener preregistro por ID
  obtenerPreregistro(tipoRegistro, id) {
    const endpoint = tipoRegistro === 'persona' ? '/personas/' : '/empresas/'
    return apiClient.get(`${endpoint}${id}/`)
  },
  
  // Confirmar preregistro
  confirmarPreregistro(tipoRegistro, id) {
    const endpoint = tipoRegistro === 'persona' ? '/personas/' : '/empresas/'
    return apiClient.patch(`${endpoint}${id}/confirmar/`)
  },
  
  // Listar todos los preregistros
  listarPersonas(params = {}) {
    return apiClient.get('/personas/', { params })
  },
  
  listarEmpresas(params = {}) {
    return apiClient.get('/empresas/', { params })
  },
}
