import os
import shutil
import tempfile
from datetime import datetime, timedelta
import mimetypes

TEMP_DIR = os.getenv('TEMP_DIR', './temp')
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 52428800))  # 50MB default

def ensure_temp_dir():
    """Cria diretório temporário se não existir."""
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

def validate_pdf(file):
    """Valida se o arquivo é um PDF válido."""
    if not file or file.filename == '':
        return False, "Nenhum arquivo enviado"
    
    # Validar extensão
    if not file.filename.lower().endswith('.pdf'):
        return False, "Arquivo deve ser um PDF"
    
    # Validar tamanho
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    
    if file_size > MAX_FILE_SIZE:
        return False, f"Arquivo muito grande. Máximo: {MAX_FILE_SIZE / 1024 / 1024:.0f}MB"
    
    # Validar magic bytes do PDF
    file.seek(0)
    header = file.read(4)
    file.seek(0)
    
    if header != b'%PDF':
        return False, "Arquivo inválido. Não é um PDF"
    
    return True, "Válido"

def save_upload(file):
    """Salva arquivo enviado em diretório temporário."""
    ensure_temp_dir()
    
    valid, msg = validate_pdf(file)
    if not valid:
        return None, msg
    
    filename = f"upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
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
