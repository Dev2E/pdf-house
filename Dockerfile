FROM python:3.13-slim

WORKDIR /app

# Copiar arquivos de requisitos
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Expor porta
EXPOSE 5000

# Comando para iniciar
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]
