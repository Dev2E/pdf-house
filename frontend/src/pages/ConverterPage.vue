<template>
  <div class="w-full bg-background min-h-screen flex flex-col font-['Inter'] antialiased">
    <!-- Main Content -->
    <main class="flex-grow max-w-[1120px] w-full mx-auto px-4 md:px-8 pt-[120px] pb-20 flex flex-col gap-12">
      <!-- Hero Section -->
      <section class="text-center flex flex-col items-center gap-3 max-w-2xl mx-auto">
        <h1 class="text-5xl font-bold text-slate-900 dark:text-slate-100">Converta seus PDFs em segundos</h1>
        <p class="text-lg text-slate-600 dark:text-slate-400">
          Ferramenta rápida e segura para transformação de documentos. Arraste, escolha o formato e processe instantaneamente.
        </p>
      </section>

      <!-- Advertisement Banner -->
      <AdBanner :show-ads="true" />

      <!-- Conversion Interface -->
      <section class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
        <!-- Main Tool Area -->
        <div class="lg:col-span-2 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 flex flex-col gap-6" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          
          <!-- Upload Drop Zone -->
          <div 
            class="border-2 border-dashed border-blue-500 hover:border-blue-600 hover:bg-blue-50 dark:hover:bg-slate-800 bg-slate-50 dark:bg-slate-800 transition-all duration-200 rounded-xl p-16 flex flex-col items-center justify-center text-center cursor-pointer group"
            @click="$refs.fileInput.click()"
            @drop="handleDrop"
            @dragover.prevent
            @dragenter.prevent
          >
            <svg class="w-12 h-12 text-blue-500 mb-3 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9.172 2.828a1 1 0 011.656 0l4 4a1 1 0 11-1.414 1.414L11 6.414V15a1 1 0 11-2 0V6.414L6.586 8.828a1 1 0 111.414-1.414l4-4z" />
            </svg>
            <h3 class="text-lg font-semibold text-slate-900 dark:text-slate-100 mb-1">Arraste e solte seu arquivo aqui</h3>
            <p class="text-sm text-slate-600 dark:text-slate-400">ou clique para procurar no seu computador</p>
            <input 
              ref="fileInput"
              type="file" 
              accept=".pdf" 
              @change="handleFileSelect"
              class="hidden"
            />
            <p v-if="selectedFile" class="mt-4 text-sm text-green-600 dark:text-green-400">
              ✓ {{ selectedFile.name }}
            </p>
          </div>

          <!-- Format Selection -->
          <div class="flex flex-col gap-3">
            <h4 class="text-lg font-semibold text-slate-900 dark:text-slate-100">Formato de Saída</h4>
            <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
              <button
                v-for="format in availableFormats"
                :key="format"
                @click="toggleFormat(format)"
                :class="[
                  'py-2 px-3 rounded-lg border-2 font-medium text-sm transition-all',
                  selectedFormats.includes(format)
                    ? 'border-blue-500 bg-blue-600 text-white dark:bg-blue-700'
                    : 'border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100 hover:border-blue-500'
                ]"
              >
                {{ format }}
              </button>
            </div>
          </div>

          <!-- Action Button -->
          <button 
            @click="handleConvert"
            :disabled="!selectedFile || selectedFormats.length === 0 || isConverting"
            :class="[
              'w-full py-3 px-6 rounded-lg font-semibold text-white transition-all flex items-center justify-center gap-2',
              isConverting || !selectedFile || selectedFormats.length === 0
                ? 'bg-slate-400 dark:bg-slate-600 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700 active:scale-95'
            ]"
            style="box-shadow: 0 4px 12px rgba(0,0,0,0.08);"
          >
            <svg v-if="!isConverting" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            <span>{{ isConverting ? 'Convertendo...' : 'Converter Agora' }}</span>
          </button>

          <!-- Status Messages -->
          <ConversionStatus 
            :status="conversionStatus"
            :error-message="errorMessage"
            :progress="conversionProgress"
            :estimated-time="estimatedTime"
            @close="resetForm"
          />

          <!-- Success Dialog -->
          <div 
            v-if="conversionStatus === 'success'"
            class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4"
            @click="resetForm"
          >
            <div 
              class="bg-white dark:bg-slate-900 rounded-xl p-8 max-w-sm w-full shadow-2xl"
              @click.stop
            >
              <div class="flex flex-col items-center gap-4">
                <div class="w-16 h-16 bg-green-100 dark:bg-green-900/30 rounded-full flex items-center justify-center">
                  <svg class="w-8 h-8 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                </div>
                
                <h3 class="text-xl font-bold text-slate-900 dark:text-slate-100">Pronto!</h3>
                <p class="text-center text-slate-600 dark:text-slate-400">Seu arquivo foi convertido com sucesso.</p>
                
                <div class="w-full flex flex-col gap-3 pt-4">
                  <button 
                    @click="resetForm"
                    class="w-full py-3 px-6 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg transition-all active:scale-95"
                  >
                    Converter Outro
                  </button>
                  <button 
                    @click="handleCloseSuccess"
                    class="w-full py-3 px-6 bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-900 dark:text-slate-100 font-semibold rounded-lg transition-all active:scale-95"
                  >
                    Fechar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Status Panel (Sidebar) -->
        <aside class="lg:col-span-1 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 flex flex-col gap-6 h-full" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <div class="border-b border-slate-200 dark:border-slate-800 pb-4 flex items-center justify-between">
            <h2 class="text-lg font-semibold text-slate-900 dark:text-slate-100">Informações</h2>
            <svg class="w-5 h-5 text-slate-400" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
            </svg>
          </div>
          
          <ul class="flex flex-col gap-4 text-sm text-slate-600 dark:text-slate-400">
            <li><strong class="text-slate-900 dark:text-slate-100">Tamanho máximo:</strong> 50 MB</li>
            <li><strong class="text-slate-900 dark:text-slate-100">Formatos:</strong> PNG, JPG, TXT, DOCX, XLSX, COMPRESS</li>
            <li><strong class="text-slate-900 dark:text-slate-100">Segurança:</strong> Arquivos deletados após 1 hora</li>
            <li><strong class="text-slate-900 dark:text-slate-100">Múltiplos formatos:</strong> Receba um ZIP</li>
          </ul>
        </aside>
      </section>

      <!-- Bottom Advertisement Banner -->
      <AdBanner :show-ads="true" />
    </main>
  </div>
</template>

<script>
import ConversionStatus from '../components/ConversionStatus.vue'
import AdBanner from '../components/AdBanner.vue'
import conversionService from '../services/conversionService.js'

export default {
  name: 'ConverterPage',
  components: {
    ConversionStatus,
    AdBanner
  },
  data() {
    return {
      selectedFile: null,
      selectedFormats: [],
      availableFormats: ['PNG', 'JPG', 'TXT', 'DOCX', 'XLSX', 'COMPRESS'],
      conversionStatus: 'idle',
      isConverting: false,
      errorMessage: '',
      conversionProgress: 0,
      estimatedTime: null,
      progressInterval: null
    }
  },
  methods: {
    handleDrop(e) {
      e.preventDefault()
      const files = e.dataTransfer.files
      if (files.length > 0) {
        const file = files[0]
        if (file.type === 'application/pdf') {
          this.selectedFile = file
        } else {
          this.errorMessage = 'Por favor, selecione um arquivo PDF'
          this.conversionStatus = 'error'
        }
      }
    },
    handleFileSelect() {
      const file = this.$refs.fileInput.files[0]
      if (file) {
        this.selectedFile = file
        this.errorMessage = ''
      }
    },
    toggleFormat(format) {
      const index = this.selectedFormats.indexOf(format)
      if (index > -1) {
        this.selectedFormats.splice(index, 1)
      } else {
        this.selectedFormats.push(format)
      }
    },
    async handleConvert() {
      if (!this.selectedFile || this.selectedFormats.length === 0) {
        this.errorMessage = 'Selecione um arquivo e pelo menos um formato'
        this.conversionStatus = 'error'
        return
      }

      this.isConverting = true
      this.conversionStatus = 'loading'
      this.errorMessage = ''
      this.conversionProgress = 0
      this.estimatedTime = 30

      // Simular progresso
      this.progressInterval = setInterval(() => {
        if (this.conversionProgress < 90) {
          this.conversionProgress += Math.random() * 20
          if (this.conversionProgress > 90) this.conversionProgress = 90
          this.estimatedTime = Math.max(1, this.estimatedTime - 1)
        }
      }, 500)

      const result = await conversionService.convertPDF(
        this.selectedFile,
        this.selectedFormats
      )

      this.isConverting = false
      clearInterval(this.progressInterval)
      this.conversionProgress = 100
      this.estimatedTime = null

      if (result.success) {
        this.conversionStatus = 'success'
        
        // Trigger download
        const url = window.URL.createObjectURL(result.data)
        const link = document.createElement('a')
        link.href = url
        
        const ext = this.selectedFormats.length === 1 
          ? this.selectedFormats[0].toLowerCase()
          : 'zip'
        link.download = `${this.selectedFile.name.replace('.pdf', '')}_converted.${ext}`
        
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
        window.URL.revokeObjectURL(url)
      } else {
        this.conversionStatus = 'error'
        this.errorMessage = result.error || 'Erro desconhecido na conversão'
      }
    },
    resetForm() {
      this.selectedFile = null
      this.selectedFormats = []
      this.conversionStatus = 'idle'
      this.errorMessage = ''
      this.conversionProgress = 0
      this.estimatedTime = null
      if (this.progressInterval) clearInterval(this.progressInterval)
    },
    handleCloseSuccess() {
      this.conversionStatus = 'idle'
    }
  }
}
</script>

<style scoped>
.background {
  background-color: #faf9ff;
}
</style>
