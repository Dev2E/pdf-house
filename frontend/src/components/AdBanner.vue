<template>
  <div v-if="showAds" class="w-full bg-slate-100 dark:bg-slate-800 p-4 my-6 rounded-lg border border-slate-200 dark:border-slate-700 flex items-center justify-center">
    <!-- Ad Container -->
    <div class="w-full max-w-[300px]">
      <div class="bg-white dark:bg-slate-900 p-3 rounded text-center">
        <!-- Google AdSense Ad -->
        <ins class="adsbygoogle"
             style="display:inline-block;width:300px;height:250px;max-width:100%"
             data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
             data-ad-slot="1234567890"></ins>
      </div>
    </div>
  </div>
  <!-- Fallback placeholder for development -->
  <div v-else-if="isDevelopment && showAds" class="w-full bg-gradient-to-r from-yellow-100 to-orange-100 dark:from-yellow-900 dark:to-orange-900 p-4 my-6 rounded-lg border-2 border-yellow-400 dark:border-yellow-600 text-center">
    <p class="text-sm text-yellow-800 dark:text-yellow-200 font-medium">📢 Espaço reservado para anúncios (Google AdSense)</p>
    <p class="text-xs text-yellow-700 dark:text-yellow-300 mt-1">Configure seu ca-pub-xxxxx para ativar anúncios reais</p>
  </div>
</template>

<script>
export default {
  name: 'AdBanner',
  props: {
    showAds: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      isDevelopment: process.env.NODE_ENV === 'development'
    }
  },
  mounted() {
    // Carregar anúncios do Google AdSense
    if (window.adsbygoogle && this.showAds) {
      try {
        (adsbygoogle = window.adsbygoogle || []).push({})
      } catch (e) {
        console.log('AdSense ainda não carregado')
      }
    }
  }
}
</script>

<style scoped>
ins.adsbygoogle {
  display: inline-block;
}
</style>
