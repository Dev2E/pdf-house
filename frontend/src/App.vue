<template>
  <div id="app" class="min-h-screen flex flex-col">
    <Header :active-page="activePage" @navigate="handleNavigate" />
    <main class="flex-grow">
      <ConverterPage v-if="activePage === 'conversor'" @error="handleError" />
      <FAQPage v-if="activePage === 'faq'" />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import ConverterPage from './pages/ConverterPage.vue'
import FAQPage from './pages/FAQPage.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    ConverterPage,
    FAQPage
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
