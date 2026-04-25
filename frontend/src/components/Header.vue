<template>
  <header class="fixed top-0 w-full z-50 border-b border-slate-200 dark:border-slate-800 shadow-sm bg-white/90 dark:bg-slate-950/90 backdrop-blur-md">
    <div class="max-w-[1120px] mx-auto px-4 md:px-8 h-16 flex justify-between items-center">
      <!-- Brand -->
      <div 
        @click="$emit('navigate', 'conversor')"
        class="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity"
      >
        <span class="text-xl font-black text-blue-600 dark:text-blue-400 tracking-tight font-['Inter'] antialiased text-slate-900 dark:text-slate-100">PDF HOUSE</span>
      </div>
      
      <!-- Navigation -->
      <nav class="hidden md:flex items-center gap-6">
        <button 
          @click="$emit('navigate', 'conversor')"
          :class="[
            'font-medium transition-all duration-200 active:scale-95',
            activePage === 'conversor' 
              ? 'text-blue-600 dark:text-blue-400 font-bold border-b-2 border-blue-600 pb-1' 
              : 'text-slate-600 dark:text-slate-400 hover:text-blue-500 hover:bg-slate-50 dark:hover:bg-slate-900'
          ]"
        >
          Conversor
        </button>
        <button 
          @click="$emit('navigate', 'faq')"
          :class="[
            'font-medium transition-all duration-200 active:scale-95',
            activePage === 'faq' 
              ? 'text-blue-600 dark:text-blue-400 font-bold border-b-2 border-blue-600 pb-1' 
              : 'text-slate-600 dark:text-slate-400 hover:text-blue-500 hover:bg-slate-50 dark:hover:bg-slate-900'
          ]"
        >
          FAQ
        </button>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  props: {
    activePage: {
      type: String,
      default: 'conversor'
    }
  },
  emits: ['navigate']
}
</script>

<style scoped>
button {
  outline: none;
}
</style>
