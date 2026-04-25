<template>
  <div id="app" class="min-h-screen flex flex-col">
    <Header :active-page="activePage" @navigate="handleNavigate" />
    <main class="flex-grow">
      <ConverterPage v-if="activePage === 'conversor'" @error="handleError" />
      <FAQPage v-if="activePage === 'faq'" />
      <TermsPage v-if="activePage === 'termos'" />
      <PrivacyPage v-if="activePage === 'privacidade'" />
      <SecurityPage v-if="activePage === 'seguranca'" />
    </main>
    <Footer @navigate="handleNavigate" />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import ConverterPage from './pages/ConverterPage.vue'
import FAQPage from './pages/FAQPage.vue'
import TermsPage from './pages/TermsPage.vue'
import PrivacyPage from './pages/PrivacyPage.vue'
import SecurityPage from './pages/SecurityPage.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    ConverterPage,
    FAQPage,
    TermsPage,
    PrivacyPage,
    SecurityPage
  },
  data() {
    return {
      activePage: 'conversor'
    }
  },
  methods: {
    handleNavigate(page) {
      this.activePage = page
    },
    handleError(error) {
      console.error('Erro:', error)
    }
  }
}
</script>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
