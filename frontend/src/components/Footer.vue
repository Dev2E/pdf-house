<template>
  <footer class="w-full border-t mt-auto border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900">
    <div class="max-w-[1120px] mx-auto px-4 py-12 flex flex-col md:flex-row justify-between items-center gap-6">
      <!-- Brand & Copyright -->
      <div class="flex flex-col gap-2 items-center md:items-start">
        <span class="text-lg font-bold text-slate-900 dark:text-white font-['Inter']">SaintPDF</span>
        <p class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400">© 2026 SaintPDF. Processamento seguro de arquivos. Limite de 50MB por conversão.</p>
        <p class="font-['Inter'] text-xs text-slate-400 dark:text-slate-500">prod by eliel</p>
      </div>
      
      <!-- Links -->
      <nav class="flex flex-wrap justify-center gap-6">
        <button 
          @click="$emit('navigate', 'termos')"
          class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none cursor-pointer bg-transparent border-none"
        >
          Termos de Uso
        </button>
        <button 
          @click="$emit('navigate', 'privacidade')"
          class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none cursor-pointer bg-transparent border-none"
        >
          Privacidade
        </button>
        <button 
          @click="$emit('navigate', 'seguranca')"
          class="font-['Inter'] text-sm text-slate-500 dark:text-slate-400 hover:text-blue-600 hover:underline transition-all focus:ring-2 focus:ring-blue-500 outline-none cursor-pointer bg-transparent border-none"
        >
          Segurança
        </button>
      </nav>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>
