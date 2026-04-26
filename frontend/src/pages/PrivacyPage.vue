<template>
  <div class="w-full bg-background min-h-screen flex flex-col font-['Inter'] antialiased">
    <!-- Main Content -->
    <main class="flex-grow max-w-3xl w-full mx-auto px-4 md:px-8 pt-[120px] pb-20 flex flex-col gap-8">
      <!-- Header -->
      <section class="text-center flex flex-col gap-3">
        <h1 class="text-5xl font-bold text-slate-900 dark:text-slate-100">Política de Privacidade</h1>
        <p class="text-lg text-slate-600 dark:text-slate-400">
          Saiba como o SaintPDF coleta, usa e protege seus dados
        </p>
      </section>

      <!-- Content -->
      <div class="prose dark:prose-invert max-w-none">
        <!-- Section 1 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">1. Informações que Coletamos</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Coletamos informações limitadas para operar nosso serviço:
          </p>
          <ul class="list-disc list-inside space-y-2 text-slate-600 dark:text-slate-400">
            <li>Arquivos PDF que você carrega (processados temporariamente)</li>
            <li>Informações do navegador (cookies e identificadores de sessão)</li>
            <li>Endereço IP para fins de segurança e análise</li>
          </ul>
        </div>

        <!-- Section 2 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">2. Como Usamos Seus Dados</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Seus dados são usados exclusivamente para:
          </p>
          <ul class="list-disc list-inside space-y-2 text-slate-600 dark:text-slate-400">
            <li>Processar suas conversões de PDF</li>
            <li>Melhorar a qualidade do serviço</li>
            <li>Manter a segurança da plataforma</li>
            <li>Análise estatística anônima</li>
          </ul>
        </div>

        <!-- Section 3 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">3. Retenção de Dados</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Os arquivos PDF que você carrega são automaticamente deletados após 1 hora. Não armazenamos seus documentos permanentemente.
          </p>
        </div>

        <!-- Section 4 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">4. Compartilhamento de Dados</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Nunca compartilhamos seus dados pessoais ou documentos com terceiros. Você tem total controle sobre seus arquivos.
          </p>
        </div>

        <!-- Section 5 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">5. Seus Direitos</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Você tem o direito de solicitar acesso, correção ou exclusão de seus dados. Entre em contato conosco para exercer esses direitos.
          </p>
        </div>

        <!-- Section 6 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">6. Contato</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Para dúvidas sobre privacidade, entre em contato conosco através do nosso formulário de suporte.
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'PrivacyPage'
}
</script>

<style scoped>
.prose {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
</style>
