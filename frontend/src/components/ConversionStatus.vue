<template>
  <div class="conversion-status" v-if="isVisible">
    <div v-if="status === 'loading'" class="status-container loading">
      <div class="spinner"></div>
      <p class="status-text">Convertendo seu PDF...</p>
    </div>
    
    <div v-if="status === 'success'" class="status-container success">
      <svg class="status-icon success-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
      </svg>
      <p class="status-text">Conversão concluída com sucesso!</p>
      <button @click="$emit('close')" class="status-button success-button">Fechar</button>
    </div>
    
    <div v-if="status === 'error'" class="status-container error">
      <svg class="status-icon error-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
      <p class="status-text">{{ errorMessage }}</p>
      <button @click="$emit('close')" class="status-button error-button">Fechar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ConversionStatus',
  props: {
    status: {
      type: String,
      required: true,
      validator: (value) => ['idle', 'loading', 'success', 'error'].includes(value)
    },
    errorMessage: {
      type: String,
      default: 'Ocorreu um erro durante a conversão'
    }
  },
  computed: {
    isVisible() {
      return this.status !== 'idle'
    }
  }
}
</script>

<style scoped>
.conversion-status {
  width: 100%;
  margin-top: 24px;
}

.status-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 24px;
  border-radius: 12px;
  text-align: center;
  border: 2px solid;
}

.status-container.loading {
  background-color: rgba(59, 130, 246, 0.1);
  border-color: #3b82f6;
  color: #1e40af;
}

.status-container.success {
  background-color: rgba(34, 197, 94, 0.1);
  border-color: #22c55e;
  color: #166534;
}

.status-container.error {
  background-color: rgba(239, 68, 68, 0.1);
  border-color: #ef4444;
  color: #991b1b;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(59, 130, 246, 0.3);
  border-top-color: #3b82f6;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.status-icon {
  width: 48px;
  height: 48px;
}

.status-icon.success-icon {
  color: #16a34a;
}

.status-icon.error-icon {
  color: #dc2626;
}

.status-text {
  margin: 0;
  font-size: 16px;
  font-weight: 500;
}

.status-button {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  color: white;
  transition: opacity 0.3s ease;
}

.status-button:hover {
  opacity: 0.8;
}

.success-button {
  background-color: #16a34a;
}

.error-button {
  background-color: #dc2626;
}
</style>
