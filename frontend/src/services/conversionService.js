import axios from 'axios'

// Detectar ambiente
const isDevelopment = window.location.hostname === 'localhost'
const API_URL = isDevelopment 
  ? 'http://localhost:5000/api'
  : `${window.location.origin}/api`

export default {
  async convertPDF(file, formats) {
    const formData = new FormData()
    formData.append('file', file)
    
    formats.forEach(format => {
      formData.append('formats', format)
    })
    
    try {
      const response = await axios.post(`${API_URL}/convert`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        responseType: 'blob'
      })
      
      return { success: true, data: response.data }
    } catch (error) {
      const errorMsg = error.response?.data?.error || error.message || 'Erro desconhecido'
      return { success: false, error: errorMsg }
    }
  },
  
  async healthCheck() {
    try {
      const response = await axios.get(`${API_URL}/health`)
      return { success: true, data: response.data }
    } catch (error) {
      return { success: false, error: error.message }
    }
  }
}
