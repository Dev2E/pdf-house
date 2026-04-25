<template>
  <div class="w-full bg-background min-h-screen flex flex-col font-['Inter'] antialiased">
    <!-- Main Content -->
    <main class="flex-grow max-w-3xl w-full mx-auto px-4 md:px-8 pt-[120px] pb-20 flex flex-col gap-8">
      <!-- Header -->
      <section class="text-center flex flex-col gap-3">
        <h1 class="text-5xl font-bold text-slate-900 dark:text-slate-100">Segurança</h1>
        <p class="text-lg text-slate-600 dark:text-slate-400">
          Saiba como o PDF HOUSE protege seus documentos e dados
        </p>
      </section>

      <!-- Content -->
      <div class="prose dark:prose-invert max-w-none">
        <!-- Section 1 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">1. Criptografia</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Todos os arquivos são transferidos usando criptografia SSL/TLS de ponta a ponta. Seus documentos estão protegidos durante o upload e o download.
          </p>
        </div>

        <!-- Section 2 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">2. Armazenamento Seguro</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Arquivos processados são armazenados temporariamente em servidores seguros com controle de acesso rigoroso. Todos os dados são deletados automaticamente após 1 hora.
          </p>
        </div>

        <!-- Section 3 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">3. Validação de Arquivo</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Verificamos a integridade de cada arquivo usando:
          </p>
          <ul class="list-disc list-inside space-y-2 text-slate-600 dark:text-slate-400">
            <li>Validação de magic bytes (assinatura de arquivo)</li>
            <li>Limite de tamanho (máximo 50 MB)</li>
            <li>Verificação de tipo MIME</li>
          </ul>
        </div>

        <!-- Section 4 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">4. Práticas de Segurança</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Implementamos:
          </p>
          <ul class="list-disc list-inside space-y-2 text-slate-600 dark:text-slate-400">
            <li>CORS para proteção contra solicitações não autorizadas</li>
            <li>Rate limiting para prevenir abuso</li>
            <li>Logs de segurança para detecção de anomalias</li>
            <li>Atualizações regulares de segurança</li>
          </ul>
        </div>

        <!-- Section 5 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">5. Conformidade</h2>
          <p class="text-slate-600 dark:text-slate-400">
            O PDF HOUSE é desenvolvido com as melhores práticas de segurança da indústria e em conformidade com padrões internacionais de proteção de dados.
          </p>
        </div>

        <!-- Section 6 -->
        <div class="bg-white dark:bg-slate-900 rounded-xl p-6 border border-slate-200 dark:border-slate-800 flex flex-col gap-4">
          <h2 class="text-2xl font-bold text-slate-900 dark:text-slate-100">6. Relatar Vulnerabilidades</h2>
          <p class="text-slate-600 dark:text-slate-400">
            Se descobrir uma vulnerabilidade de segurança, por favor entre em contato conosco imediatamente através do formulário de suporte. Levaremos sua preocupação a sério.
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'SecurityPage'
}
</script>

<style scoped>
.prose {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
</style>
