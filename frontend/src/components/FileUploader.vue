<template>
  <div class="uploader" @drop="handleDrop" @dragover.prevent @dragenter.prevent>
    <div class="upload-area" :class="{ 'drag-over': isDragging }">
      <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
      </svg>
      <h3>Arraste seu PDF aqui</h3>
      <p>ou</p>
      <label class="file-input-label">
        <input 
          ref="fileInput"
          type="file" 
          accept=".pdf" 
          @change="handleFileSelect"
          class="file-input"
        />
        <span class="browse-button">Escolher arquivo</span>
      </label>
      <p class="file-info" v-if="selectedFile">
        Arquivo: <strong>{{ selectedFile.name }}</strong> ({{ formatFileSize(selectedFile.size) }})
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FileUploader',
  data() {
    return {
      isDragging: false,
      selectedFile: null
    }
  },
  methods: {
    handleDrop(e) {
      e.preventDefault()
      e.stopPropagation()
      this.isDragging = false
      
      const files = e.dataTransfer.files
      if (files.length > 0) {
        const file = files[0]
        if (file.type === 'application/pdf') {
          this.selectedFile = file
          this.$emit('file-selected', file)
        } else {
          this.$emit('error', 'Por favor, selecione um arquivo PDF')
        }
      }
    },
    handleFileSelect() {
      const file = this.$refs.fileInput.files[0]
      if (file) {
        this.selectedFile = file
        this.$emit('file-selected', file)
      }
    },
    formatFileSize(bytes) {
      if (bytes === 0) return '0 Bytes'
      const k = 1024
      const sizes = ['Bytes', 'KB', 'MB', 'GB']
      const i = Math.floor(Math.log(bytes) / Math.log(k))
      return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i]
    }
  }
}
</script>

<style scoped>
.uploader {
  width: 100%;
}

.upload-area {
  border: 2px dashed #cbd5e1;
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #f8fafc;
}

.upload-area:hover {
  border-color: #0ea5e9;
  background-color: #f0f9ff;
}

.upload-area.drag-over {
  border-color: #0284c7;
  background-color: #e0f2fe;
  transform: scale(1.02);
}

.upload-icon {
  width: 48px;
  height: 48px;
  margin: 0 auto 16px;
  color: #0ea5e9;
}

.upload-area h3 {
  margin: 0 0 8px;
  color: #1e293b;
  font-size: 18px;
  font-weight: 600;
}

.upload-area p {
  margin: 8px 0;
  color: #64748b;
  font-size: 14px;
}

.file-input {
  display: none;
}

.file-input-label {
  display: inline-block;
}

.browse-button {
  display: inline-block;
  padding: 10px 24px;
  margin-top: 8px;
  background-color: #0ea5e9;
  color: white;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.browse-button:hover {
  background-color: #0284c7;
}

.file-info {
  margin-top: 16px;
  color: #059669;
  font-size: 14px;
}

.file-info strong {
  color: #047857;
}
</style>
