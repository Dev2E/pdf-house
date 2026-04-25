FROM python:3.13-slim

WORKDIR /app

# Instalar dependências do sistema (poppler para pdf2image)
RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de requisitos
COPY backend/requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do backend
COPY backend/ .

# Expor porta
EXPOSE 5000

# Comando para iniciar
CMD ["python", "app.py"]
