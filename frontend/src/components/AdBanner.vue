<template>
  <div v-if="showAds" class="w-full bg-slate-100 dark:bg-slate-800 p-2 my-4 rounded-lg border border-slate-200 dark:border-slate-700 flex items-center justify-center">
    <!-- Ad Container - Smaller Size -->
    <div class="w-full max-w-[320px] md:max-w-[336px]">
      <div class="bg-white dark:bg-slate-900 p-2 rounded text-center">
        <!-- Google AdSense Ad - Mobile optimized -->
        <ins class="adsbygoogle"
             style="display:inline-block;width:320px;height:50px;max-width:100%"
             data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
             data-ad-slot="1234567890"></ins>
      </div>
    </div>
  </div>
  <!-- Fallback placeholder for development -->
  <div v-else-if="isDevelopment && showAds" class="w-full bg-gradient-to-r from-yellow-100 to-orange-100 dark:from-yellow-900 dark:to-orange-900 p-2 my-4 rounded-lg border border-yellow-400 dark:border-yellow-600 text-center max-w-[336px] mx-auto">
    <p class="text-xs text-yellow-800 dark:text-yellow-200 font-medium">📢 Anúncio</p>
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
