<template>
  <footer class="w-full border-t mt-auto border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900">
    <div class="max-w-[1120px] mx-auto px-4 py-12 flex flex-col md:flex-row justify-between items-center gap-6">
      <!-- Brand & Copyright -->
      <div class="flex flex-col gap-2 items-center md:items-start">
        <span class="text-lg font-bold text-slate-900 dark:text-white font-['Inter']">PDF Pro</span>
        <p class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400">© 2026 PDF Pro. Processamento seguro de arquivos. Limite de 50MB por conversão.</p>
        <p class="font-['Inter'] text-xs text-slate-400 dark:text-slate-500">prod by eliel</p>
      </div>
      
      <!-- Links -->
      <nav class="flex flex-wrap justify-center gap-6">
        <a class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none" href="#">
          Termos de Uso
        </a>
        <a class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none" href="#">
          Privacidade
        </a>
        <a class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none" href="#">
          Segurança
        </a>
        <a class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none" href="#">
          Contato
        </a>
      </nav>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>
