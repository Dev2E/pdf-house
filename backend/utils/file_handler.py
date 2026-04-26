import os
from datetime import datetime, timedelta
from pathlib import Path

TEMP_DIR = os.path.abspath(os.getenv('TEMP_DIR', './temp'))
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 52428800))  # 50MB default

# Extensões permitidas e seus magic bytes de validação (quando aplicável)
ALLOWED_EXTENSIONS = {
    'pdf', 'png', 'jpg', 'jpeg', 'webp', 'gif', 'bmp',
    'docx', 'xlsx', 'pptx', 'txt', 'csv'
}

# Magic bytes para validação de tipos binários
MAGIC_BYTES = {
    'pdf':  (b'%PDF', 4),
    'png':  (b'\x89PNG', 4),
    'jpg':  (b'\xff\xd8\xff', 3),
    'jpeg': (b'\xff\xd8\xff', 3),
    'gif':  (b'GIF8', 4),
    'webp': (b'RIFF', 4),
    'bmp':  (b'BM', 2),
    # Formatos Office e texto não têm magic bytes simples — validamos só extensão
}

def ensure_temp_dir():
    """Cria diretório temporário se não existir."""
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

def get_file_extension(filename):
    """Retorna extensão sem ponto em lowercase."""
    return Path(filename).suffix.lstrip('.').lower()

def validate_file(file):
    """Valida tipo, tamanho e integridade básica do arquivo enviado."""
    if not file or file.filename == '':
        return False, "Nenhum arquivo enviado"

    ext = get_file_extension(file.filename)
    if ext not in ALLOWED_EXTENSIONS:
        return False, f"Tipo de arquivo não suportado: .{ext}"

    # Validar tamanho
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    if file_size > MAX_FILE_SIZE:
        return False, f"Arquivo muito grande. Máximo: {MAX_FILE_SIZE / 1024 / 1024:.0f}MB"

    # Validar magic bytes quando disponível
    if ext in MAGIC_BYTES:
        magic, length = MAGIC_BYTES[ext]
        header = file.read(length)
        file.seek(0)
        if not header.startswith(magic):
            return False, f"Arquivo inválido ou corrompido"

    return True, "Válido"

def save_upload(file):
    """Salva arquivo enviado em diretório temporário."""
    ensure_temp_dir()

    valid, msg = validate_file(file)
    if not valid:
        return None, msg

    ext = get_file_extension(file.filename)
    filename = f"upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
    filepath = os.path.join(TEMP_DIR, filename)

    file.save(filepath)
    return filepath, "Arquivo salvo com sucesso"

def cleanup_temp():
    """Remove arquivos temporários mais antigos que 1 hora."""
    if not os.path.exists(TEMP_DIR):
        return
    
    cutoff_time = datetime.now() - timedelta(hours=1)
    
    for filename in os.listdir(TEMP_DIR):
        filepath = os.path.join(TEMP_DIR, filename)
        try:
            file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            if file_time < cutoff_time:
                os.remove(filepath)
        except Exception as e:
            print(f"Erro ao deletar {filepath}: {e}")

def remove_file(filepath):
    """Remove arquivo específico."""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        print(f"Erro ao remover {filepath}: {e}")

def create_output_dir():
    """Cria diretório para arquivos de saída."""
    ensure_temp_dir()
    output_dir = os.path.join(TEMP_DIR, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir
