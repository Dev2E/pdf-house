# 📺 Configurando Google AdSense

## Como Ativar Anúncios no PDF Pro

### 1. Registrar no Google AdSense
1. Acesse [Google AdSense](https://www.google.com/adsense/start/)
2. Clique em "Começar" e faça login com sua conta Google
3. Adicione seu site (localhost:5174 ou seu domínio)
4. Aguarde a aprovação (24-72 horas)

### 2. Obter seu ca-pub-xxxxx
Após aprovação, você receberá um ID de publicador:
- **Exemplo:** `ca-pub-1234567890123456`

### 3. Atualizar os arquivos

**Arquivo 1: `frontend/index.html`**
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-SEU_ID_AQUI"
    crossorigin="anonymous"></script>
```

**Arquivo 2: `frontend/src/config/monetization.js`**
```javascript
export const ADSENSE_CONFIG = {
  clientId: 'ca-pub-SEU_ID_AQUI',  // ← Coloque aqui
  adSlots: {
    headerBanner: 'SLOT_ID_1',      // ← IDs dos slots (obtenha no AdSense)
    // ...
  }
}
```

### 4. Obter IDs dos Slots de Anúncio
No seu painel AdSense:
1. Vá para **Anúncios** → **Por tamanho**
2. Crie anúncios de:
   - `728x90` (Leaderboard - topo e rodapé)
   - `300x250` (Medium Rectangle - sidebar)
3. Copie os IDs dos slots

### 5. Localizações dos Anúncios

**Atualmente configurado em:**
- 📍 **Topo da página** (após hero section) - Leaderboard 728x90
- 📍 **Fim da página** (antes do rodapé) - Leaderboard 728x90

---

## 💰 Estimativa de Ganhos

### CPM por Região
- **Brasil:** $0.50 - $1.50
- **EUA/Canada:** $5.00 - $15.00
- **Europa:** $2.00 - $8.00

### Exemplo Brasil
```
1,000 visitantes/mês
× 2 anúncios por página
= 2,000 impressões

CPM: $1.00 (Brasil)
Ganho: (2,000 / 1,000) × $1.00 = $2.00/mês

Com crescimento:
- 10,000 visitantes = $20/mês
- 50,000 visitantes = $100/mês
- 100,000 visitantes = $200/mês
```

---

## ⚙️ Configuração Avançada

### Desabilitar Anúncios para Teste
```javascript
// frontend/src/config/monetization.js
export const ADSENSE_CONFIG = {
  enabled: false  // ← Anúncios desabilitados
}
```

### Adicionar Mais Localizações
```vue
<!-- frontend/src/pages/ConverterPage.vue -->
<AdBanner :show-ads="true" />  <!-- Adicionar em qualquer lugar -->
```

### Ocultar para Usuários Premium
```vue
<AdBanner :show-ads="!isPremiumUser" />
```

---

## 📋 Checklist de Configuração

- [ ] Registrado no Google AdSense
- [ ] Aprovado pelo Google (aguarde 24-72h)
- [ ] Obteve ca-pub-xxxxx
- [ ] Criou slots de anúncio (728x90, 300x250)
- [ ] Atualizou `frontend/index.html`
- [ ] Atualizou `frontend/src/config/monetization.js`
- [ ] Testou os anúncios no localhost
- [ ] Fez deploy do site
- [ ] Habilitou `ADSENSE_CONFIG.enabled = true`

---

## 🚨 Dicas Importantes

1. **Não clique nos seus próprios anúncios** (violação de políticas)
2. **Não peça para outros clicarem** (banimento)
3. **Aguarde 24h antes de otimizar** (dados precisos)
4. **Máximo 3 anúncios por página** (melhor UX)
5. **Revise as políticas do AdSense** (essencial)

---

## 📞 Suporte

**Problemas comuns:**
- Anúncios não aparecem: Aguarde aprovação do Google
- "Anúncios não disponíveis": Tente em outro país/região
- Ganhos baixos: Aumente o tráfego, mude localização dos anúncios

---

## 🔗 Links Úteis

- [Google AdSense Help](https://support.google.com/adsense)
- [Ad Formats Guide](https://support.google.com/adsense/answer/6002575)
- [AdSense Policies](https://support.google.com/adsense/answer/48182)
