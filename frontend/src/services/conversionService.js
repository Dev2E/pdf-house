import axios from 'axios'

// Usar URL do backend em produção
const API_URL = 'https://pdf-house.onrender.com/api'

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
      // Blob error response precisa ser lido como texto
      let errorMsg = error.message || 'Erro desconhecido'
      if (error.response?.data instanceof Blob) {
        try {
          const text = await error.response.data.text()
          const json = JSON.parse(text)
          errorMsg = json.error || errorMsg
        } catch {
          errorMsg = `Erro ${error.response.status}`
        }
      } else if (error.response?.data?.error) {
        errorMsg = error.response.data.error
      }
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
