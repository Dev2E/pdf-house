<template>
  <div 
    v-if="showBanner"
    class="fixed bottom-0 left-0 right-0 z-40 bg-slate-900 dark:bg-slate-950 border-t border-slate-700 dark:border-slate-800 shadow-2xl"
  >
    <div class="max-w-[1120px] mx-auto px-4 md:px-8 py-4 flex flex-col md:flex-row items-center justify-between gap-4">
      <!-- Texto -->
      <div class="flex-1">
        <p class="text-sm text-slate-300 dark:text-slate-400">
          Usamos cookies para melhorar sua experiência e analisar o uso do site. Ao continuar navegando, você concorda com nossa 
          <button 
            @click="$emit('navigate', 'privacidade')"
            class="text-blue-400 hover:text-blue-300 underline cursor-pointer"
          >
            política de privacidade
          </button>.
        </p>
      </div>

      <!-- Botões -->
      <div class="flex gap-3 flex-shrink-0">
        <button 
          @click="rejectCookies"
          class="px-4 py-2 rounded-lg border border-slate-600 dark:border-slate-700 text-slate-300 dark:text-slate-400 hover:bg-slate-800 dark:hover:bg-slate-800 transition-all text-sm font-medium"
        >
          Rejeitar
        </button>
        <button 
          @click="acceptCookies"
          class="px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white transition-all text-sm font-medium"
        >
          Aceitar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CookieBanner',
  data() {
    return {
      showBanner: false
    }
  },
  mounted() {
    // Verificar se já aceitou cookies
    const cookieConsent = localStorage.getItem('cookieConsent')
    if (!cookieConsent) {
      this.showBanner = true
    }
  },
  methods: {
    acceptCookies() {
      localStorage.setItem('cookieConsent', 'accepted')
      this.showBanner = false
      // Aqui você pode inicializar Google Analytics ou outros serviços
    },
    rejectCookies() {
      localStorage.setItem('cookieConsent', 'rejected')
      this.showBanner = false
    }
  }
}
</script>

<style scoped>
</style>
