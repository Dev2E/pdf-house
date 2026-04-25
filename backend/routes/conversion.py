from flask import Blueprint, request, jsonify, send_file
import os
import zipfile
from werkzeug.utils import secure_filename
from pathlib import Path

from converters.pdf_converter import PDFConverter
from utils.file_handler import save_upload, remove_file, create_output_dir

conversion_bp = Blueprint('conversion', __name__, url_prefix='/api')

ALLOWED_FORMATS = ['PNG', 'JPG', 'TXT', 'DOCX', 'XLSX', 'COMPRESS']

@conversion_bp.route('/convert', methods=['POST'])
def convert_pdf():
    """Endpoint para converter PDF em múltiplos formatos."""
    
    # Validar request
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    if 'formats' not in request.form:
        return jsonify({'error': 'Nenhum formato selecionado'}), 400
    
    file = request.files['file']
    formats = request.form.getlist('formats')
    
    # Debug log
    print(f"DEBUG: Formatos recebidos: {formats}, tipos: {[type(f) for f in formats]}")
    
    # Validar formatos
    invalid_formats = [f for f in formats if f.upper() not in ALLOWED_FORMATS]
    if invalid_formats:
        print(f"DEBUG: Formatos inválidos: {invalid_formats}")
        return jsonify({'error': f'Formatos inválidos: {invalid_formats}'}), 400
    
    # Salvar arquivo enviado
    filepath, msg = save_upload(file)
    if not filepath:
        return jsonify({'error': msg}), 400
    
    # Criar diretório de output
    output_dir = create_output_dir()
    
    try:
        converter = PDFConverter(filepath)
        output_files = []
        errors = []
        
        for format_type in formats:
            format_upper = format_type.upper()
            
            if format_upper in ['PNG', 'JPG']:
                files, error = converter.to_images(format=format_upper)
            elif format_upper == 'TXT':
                files, error = converter.to_text()
            elif format_upper == 'DOCX':
                files, error = converter.to_docx()
            elif format_upper == 'XLSX':
                files, error = converter.to_xlsx()
            elif format_upper == 'COMPRESS':
                files, error = converter.compress_pdf()
            
            if error:
                errors.append(f"{format_upper}: {error}")
            else:
                output_files.extend(files)
        
        # Remover arquivo original
        remove_file(filepath)
        
        if not output_files:
            return jsonify({'error': 'Falha na conversão: ' + ' | '.join(errors)}), 500
        
        # Se um único arquivo, retornar direto
        if len(output_files) == 1:
            file_path = output_files[0]
            filename = os.path.basename(file_path)
            return send_file(file_path, as_attachment=True, download_name=filename)
        
        # Se múltiplos arquivos, retornar ZIP
        zip_filename = f"{Path(filepath).stem}_converted.zip"
        zip_path = os.path.join(output_dir, zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in output_files:
                arcname = os.path.basename(file_path)
                zipf.write(file_path, arcname=arcname)
        
        # Limpar arquivos individuais
        for file_path in output_files:
            remove_file(file_path)
        
        return send_file(zip_path, as_attachment=True, download_name=zip_filename)
    
    except Exception as e:
        import traceback
        print(f"ERRO GERAL NA CONVERSÃO: {str(e)}")
        print(traceback.format_exc())
        remove_file(filepath)
        return jsonify({'error': f'Erro no servidor: {str(e)}'}), 500

@conversion_bp.route('/health', methods=['GET'])
def health_check():
    """Verificar saúde da API."""
    return jsonify({'status': 'ok'}), 200
