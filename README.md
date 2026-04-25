# Conversor PDF - Aplicação Web

Aplicação web para converter PDFs em múltiplos formatos (PNG, JPG, TXT, DOCX, XLSX, PPTX) com interface Vue.js e backend Flask.

## 🎯 Features

- ✅ Upload de PDF com drag-and-drop
- ✅ Conversão para 6 formatos diferentes
- ✅ Seleção de múltiplos formatos (download ZIP)
- ✅ Interface responsiva e moderna
- ✅ Processamento seguro com limpeza automática
- ✅ Limite de tamanho (50MB)
- ✅ Sem autenticação necessária

## 🛠️ Tecnologias

### Backend
- **Python 3.8+** com Flask
- **PyPDF2** - leitura de PDFs
- **pdf2image** - conversão para imagens
- **python-docx** - geração de DOCX
- **openpyxl** - geração de XLSX
- **python-pptx** - geração de PPTX
- **Flask-CORS** - comunicação frontend-backend

### Frontend
- **Vue 3** com Composition API
- **Vite** - build tool
- **Axios** - requisições HTTP
- **CSS 3** com design responsivo

## 📋 Pré-requisitos

- Node.js 16+ (para frontend)
- Python 3.8+ (para backend)
- pip (gerenciador de pacotes Python)

## 🚀 Instalação e Execução

### 1. Backend (Flask)

```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python app.py
```

O servidor Flask estará disponível em `http://localhost:5000`

### 2. Frontend (Vue.js)

```bash
cd frontend

# Instalar dependências
npm install

# Executar servidor de desenvolvimento
npm run dev
```

O frontend estará disponível em `http://localhost:5173`

## 📁 Estrutura do Projeto

```
meu_app/
├── backend/
│   ├── app.py                      # Aplicação Flask principal
│   ├── requirements.txt             # Dependências Python
│   ├── .env                        # Variáveis de ambiente
│   ├── routes/
│   │   └── conversion.py           # Rotas de conversão
│   ├── converters/
│   │   └── pdf_converter.py        # Lógica de conversão
│   ├── utils/
│   │   └── file_handler.py         # Manipulação de arquivos
│   └── temp/                       # Arquivos temporários (gerado)
│
├── frontend/
│   ├── index.html                  # HTML principal
│   ├── package.json                # Dependências Node.js
│   ├── vite.config.js              # Configuração Vite
│   ├── src/
│   │   ├── main.js                 # Entrada da aplicação
│   │   ├── App.vue                 # Componente raiz
│   │   ├── style.css               # Estilos globais
│   │   ├── components/
│   │   │   ├── FileUploader.vue    # Upload com drag-drop
│   │   │   ├── FormatSelector.vue  # Seletor de formatos
│   │   │   └── ConversionStatus.vue# Status da conversão
│   │   ├── services/
│   │   │   └── conversionService.js# Comunicação API
│   │   └── assets/                 # Recursos (imagens, fonts)
│   └── public/                     # Assets públicos
│
├── README.md                       # Este arquivo
└── .gitignore                      # Arquivos ignorados no Git
```

## 🔌 API Endpoints

### POST `/api/convert`
Converte um PDF para os formatos selecionados.

**Request:**
```
Content-Type: multipart/form-data

file: <arquivo PDF>
formats: PNG, JPG, TXT, DOCX, XLSX, PPTX (múltiplos valores)
```

**Response:**
- Um arquivo (PNG/JPG/TXT/DOCX/XLSX/PPTX) - se um formato
- ZIP com múltiplos arquivos - se vários formatos

**Errors:**
- 400: Arquivo inválido ou formato não suportado
- 500: Erro na conversão

### GET `/api/health`
Verifica se a API está funcionando.

**Response:**
```json
{
  "status": "ok"
}
```

## ⚙️ Configurações

Edite `backend/.env` para alterar:

```env
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000
TEMP_DIR=./temp
MAX_FILE_SIZE=52428800  # 50MB em bytes
```

## 🧪 Testando

### Teste do Backend (cURL)
```bash
curl -X POST http://localhost:5000/api/convert \
  -F "file=@documento.pdf" \
  -F "formats=PNG" \
  -F "formats=TXT" \
  -o resultado.zip
```

### Teste do Frontend
1. Acesse `http://localhost:5173`
2. Arraste um PDF ou clique para selecionar
3. Escolha os formatos desejados
4. Clique em "Converter"
5. O arquivo será baixado automaticamente

## 📊 Formatos Suportados

| Formato | Descrição | Casos de Uso |
|---------|-----------|-------------|
| **PNG** | Imagem com fundo transparente | Preservação de qualidade |
| **JPG** | Imagem comprimida | Tamanho reduzido |
| **TXT** | Texto simples | Edição e cópia de texto |
| **DOCX** | Documento Word | Compatibilidade Office |
| **XLSX** | Planilha Excel | Análise de dados |
| **PPTX** | Apresentação PowerPoint | Slides por página |

## 🔒 Segurança

- ✅ Validação de MIME type
- ✅ Limite de tamanho de arquivo (50MB)
- ✅ Limpeza automática de arquivos temporários
- ✅ Nomes de arquivo sanitizados
- ✅ CORS configurado

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'pdf2image'"
```bash
pip install -r requirements.txt
```

### Erro: "Connection refused" (Frontend não conecta ao Backend)
- Certifique-se de que o servidor Flask está rodando na porta 5000
- Verifique as configurações de CORS em `backend/app.py`
- Limpe o cache do navegador

### Erro: "File too large"
- Limite máximo é 50MB
- Configure `MAX_FILE_SIZE` em `backend/.env`

## 📦 Build para Produção

### Frontend
```bash
cd frontend
npm run build
# Arquivos em: frontend/dist/
```

### Backend
```bash
# Usar wsgiref ou Gunicorn para produção
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 backend.app:app
```

## 🔄 Próximas Melhorias

- [ ] Autenticação e histórico de usuário
- [ ] Upload em lote
- [ ] Preview de páginas do PDF
- [ ] OCR para PDFs com imagens
- [ ] Rate limiting
- [ ] Integração com cloud storage (S3/Azure)
- [ ] API de processamento assíncrono (Celery)

## 📝 Licença

Este projeto é de código aberto e está disponível para uso pessoal e educacional.

## 👨‍💻 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.

---

**Desenvolvido em 2026** 🚀
