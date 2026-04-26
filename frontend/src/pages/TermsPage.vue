<template>
  <div class="w-full bg-background min-h-screen flex flex-col font-['Inter'] antialiased">
    <!-- Main Content -->
    <main class="flex-grow max-w-3xl w-full mx-auto px-4 md:px-8 pt-[120px] pb-20 flex flex-col gap-8">
      <!-- Header -->
      <section class="text-center flex flex-col gap-3">
        <h1 class="text-5xl font-bold text-slate-900 dark:text-slate-100">Termos de Uso</h1>
        <p class="text-lg text-slate-600 dark:text-slate-400">
          Leia nossos termos e condições antes de usar o SaintPDF
        </p>
      </section>

      <!-- Content -->
      <div class="prose dark:prose-invert max-w-none">
        <!-- Section 1 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">1. Aceitação dos Termos</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Ao acessar e utilizar o SaintPDF, você concorda em cumprir com estes termos de uso. Se você não concordar com qualquer parte desses termos, por favor não utilize o serviço.
          </p>
        </div>

        <!-- Section 2 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">2. Uso Permitido</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Você concorda em usar o SaintPDF apenas para fins legais e de forma que não infrinja os direitos de terceiros ou restrinja o uso e aproveitamento do serviço por terceiros.
          </p>
          <ul class="list-disc list-inside space-y-2 text-slate-600 dark:text-slate-400">
            <li>Você não pode enviar malware ou conteúdo prejudicial</li>
            <li>Você não pode usar para fins comerciais sem permissão</li>
            <li>Você não pode tentar contornar as limitações de segurança</li>
          </ul>
        </div>

        <!-- Section 3 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">3. Limitação de Responsabilidade</h2>
          <p class="text-slate-600 dark:text-slate-400">
            O SaintPDF é fornecido "como está" sem garantias de qualquer tipo. Não garantimos que o serviço será ininterrupto ou livre de erros.
          </p>
        </div>

        <!-- Section 4 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">4. Modificações dos Termos</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Reservamo-nos o direito de modificar estes termos a qualquer momento. Suas alterações entrarão em vigor imediatamente após serem publicadas no site.
          </p>
        </div>

        <!-- Section 5 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">5. Contato</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Se tiver dúvidas sobre estes termos, entre em contato conosco através do nosso formulário de suporte.
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'TermsPage'
}
</script>

<style scoped>
.prose {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
</style>
