import axios from 'axios'

// Usar URLs relativas - funciona em qualquer host
const API_URL = '/api'

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
