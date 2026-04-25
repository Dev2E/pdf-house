# 🚀 Guia Completo de Deploy

## ✅ Status do Deploy

### Frontend (Vercel)
- **Status:** ✅ DEPLOYADO
- **URL:** https://frontend-ten-psi-21.vercel.app
- **GitHub:** Conectado automaticamente

### Backend (Render.com - Próximo passo)
- **Status:** ⏳ PRONTO PARA DEPLOY
- **Próximo passo:** Conectar ao Render.com

---

## 📋 Pré-requisitos

✅ Código disponível no GitHub: https://github.com/Dev2E/pdf-house
✅ Arquivo Dockerfile criado
✅ Arquivo railway.json criado
✅ requirements.txt na raiz

---

## 🎯 Deploy Backend no Render.com (2 min)

### Passo 1: Acesse Render.com
1. Vá para https://render.com
2. Clique em **"Sign up with GitHub"**
3. Autorize o acesso ao seu GitHub
4. Confirme e crie conta

### Passo 2: Criar novo Web Service
1. Dashboard → **"New"** → **"Web Service"**
2. Selecione seu repositório `pdf-house`
3. Configure:
   - **Name:** `pdf-converter-api` (ou seu nome)
   - **Environment:** `Docker` (será detectado automaticamente)
   - **Region:** `Ohio` (ou sua região)
   - **Branch:** `main`
   - **Build Command:** (deixar vazio - Docker fará tudo)
   - **Start Command:** (deixar vazio)

### Passo 3: Configurar Variáveis de Ambiente
⚠️ Clique em **"Advanced"** e adicione:
```
FLASK_ENV=production
```

### Passo 4: Deploy
1. Clique em **"Deploy"**
2. Aguarde 2-5 minutos ⏳
3. Você receberá uma URL como:
   ```
   https://pdf-converter-api.onrender.com
   ```

---

## 🔗 Conectar Frontend + Backend

Após obter a URL do Render, atualize o frontend:

### Opção 1: Via Vercel (Recomendado)
1. Vá para https://vercel.com
2. Projeto `frontend` → **Settings** → **Environment Variables**
3. Adicione:
   ```
   VITE_API_URL=https://pdf-converter-api.onrender.com/api
   ```
4. Redeploy automaticamente

### Opção 2: Editar diretamente
1. Edite `frontend/src/services/conversionService.js`:
   ```javascript
   const API_URL = 'https://pdf-converter-api.onrender.com/api'
   ```
2. Commit e push:
   ```bash
   git add .
   git commit -m "Update API URL for production"
   git push origin main
   ```
3. Vercel redeploya automaticamente

---

## ✨ Resultado Final

```
┌─────────────────────────────────────┐
│   Frontend (Vercel)                 │
│  frontend-ten-psi-21.vercel.app     │
└────────────────┬────────────────────┘
                 │
            HTTP Requests
                 │
                 ▼
┌─────────────────────────────────────┐
│   Backend (Render)                  │
│  pdf-converter-api.onrender.com/api │
└─────────────────────────────────────┘
```

---

## 🔧 Troubleshooting

**Erro: "Cannot connect to API"**
- ✅ Verifique se o Render está rodando (azul)
- ✅ Verifique a URL correta em `conversionService.js`
- ✅ Verifique CORS em `backend/app.py`

**Erro: "Build failed on Render"**
- ✅ Verifique Dockerfile está na raiz
- ✅ Verifique requirements.txt existe
- ✅ Verifique permissões de arquivo

**App lento no Render**
- ✅ Normal para plano grátis (sem payment)
- ✅ Upgrade para "Starter" ($7/mês) para melhor performance

---

## 💡 Próximos Passos

- [ ] Deploy no Render (5 minutos)
- [ ] Testar conversão de PDF
- [ ] Registrar no Google AdSense
- [ ] Adicionar domínio customizado
- [ ] Configurar CI/CD automático

---

## 📞 Links Úteis

- [Render Docs](https://render.com/docs)
- [Vercel Docs](https://vercel.com/docs)
- [GitHub](https://github.com/Dev2E/pdf-house)

---

**Status:** ✅ Pronto para produção!

Qualquer dúvida, pergunte! 🚀
