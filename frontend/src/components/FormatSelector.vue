<template>
  <div class="format-selector">
    <h3>Selecione os formatos:</h3>
    <div class="formats-grid">
      <label class="format-option" v-for="format in availableFormats" :key="format">
        <input 
          type="checkbox" 
          :value="format" 
          v-model="selectedFormats"
          @change="emitSelection"
        />
        <span class="format-name">{{ format }}</span>
        <span class="format-icon">{{ getFormatIcon(format) }}</span>
      </label>
    </div>
    <p class="format-info">{{ selectedFormats.length }} formato(s) selecionado(s)</p>
  </div>
</template>

<script>
export default {
  name: 'FormatSelector',
  data() {
    return {
      availableFormats: ['PNG', 'JPG', 'TXT', 'DOCX', 'XLSX', 'PPTX'],
      selectedFormats: ['PNG']
    }
  },
  methods: {
    emitSelection() {
      if (this.selectedFormats.length === 0) {
        this.$emit('error', 'Selecione pelo menos um formato')
        this.selectedFormats = ['PNG']
        return
      }
      this.$emit('formats-selected', this.selectedFormats)
    },
    getFormatIcon(format) {
      const icons = {
        'PNG': '🖼️',
        'JPG': '🖼️',
        'TXT': '📄',
        'DOCX': '📝',
        'XLSX': '📊',
        'PPTX': '🎯'
      }
      return icons[format] || '📦'
    }
  },
  mounted() {
    this.emitSelection()
  }
}
</script>

<style scoped>
.format-selector {
  width: 100%;
}

.format-selector h3 {
  margin: 0 0 16px;
  color: #1e293b;
  font-size: 16px;
  font-weight: 600;
}

.formats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 12px;
  margin-bottom: 16px;
}

.format-option {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #f8fafc;
}

.format-option:hover {
  border-color: #0ea5e9;
  background-color: #f0f9ff;
}

.format-option input {
  cursor: pointer;
  width: 18px;
  height: 18px;
}

.format-option input:checked {
  accent-color: #0ea5e9;
}

.format-option input:checked + .format-name {
  color: #0ea5e9;
  font-weight: 600;
}

.format-name {
  flex: 1;
  font-size: 14px;
  color: #475569;
  transition: color 0.3s ease;
}

.format-icon {
  font-size: 18px;
}

.format-info {
  margin: 0;
  font-size: 13px;
  color: #64748b;
}
</style>
