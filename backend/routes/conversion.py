from flask import Blueprint, request, jsonify, send_file
import os
import zipfile
import traceback
from pathlib import Path

from converters.pdf_converter import PDFConverter
from converters.image_converter import ImageConverter
from converters.document_converter import DocumentConverter
from utils.file_handler import save_upload, remove_file, create_output_dir, get_file_extension

conversion_bp = Blueprint('conversion', __name__, url_prefix='/api')

# Formatos de saída disponíveis por extensão do arquivo de entrada
SUPPORTED_CONVERSIONS = {
    'pdf':  ['PNG', 'JPG', 'TXT', 'DOCX', 'XLSX', 'COMPRESS'],
    'png':  ['PDF', 'JPG', 'WEBP'],
    'jpg':  ['PDF', 'PNG', 'WEBP'],
    'jpeg': ['PDF', 'PNG', 'WEBP'],
    'webp': ['PDF', 'PNG', 'JPG'],
    'gif':  ['PDF', 'PNG', 'JPG'],
    'bmp':  ['PDF', 'PNG', 'JPG'],
    'docx': ['PDF', 'TXT'],
    'xlsx': ['PDF', 'CSV', 'TXT'],
    'pptx': ['PDF', 'TXT'],
    'txt':  ['PDF', 'DOCX'],
    'csv':  ['XLSX', 'TXT'],
}


def _run_conversion(filepath, file_ext, format_upper):
    """Roteia a conversão para o conversor correto e retorna (files, error)."""

    # ── PDF ──────────────────────────────────────────────────────────────
    if file_ext == 'pdf':
        converter = PDFConverter(filepath)
        if format_upper in ('PNG', 'JPG'):
            return converter.to_images(format=format_upper)
        if format_upper == 'TXT':
            return converter.to_text()
        if format_upper == 'DOCX':
            return converter.to_docx()
        if format_upper == 'XLSX':
            return converter.to_xlsx()
        if format_upper == 'COMPRESS':
            return converter.compress_pdf()

    # ── Imagens ──────────────────────────────────────────────────────────
    if file_ext in ('png', 'jpg', 'jpeg', 'webp', 'gif', 'bmp'):
        converter = ImageConverter(filepath)
        if format_upper == 'PDF':
            return converter.to_pdf()
        return converter.to_image(format=format_upper)

    # ── Documentos / Planilhas / Texto ───────────────────────────────────
    converter = DocumentConverter(filepath)

    if file_ext == 'docx':
        if format_upper == 'PDF':
            return converter.docx_to_pdf()
        if format_upper == 'TXT':
            return converter.docx_to_txt()

    if file_ext == 'xlsx':
        if format_upper == 'PDF':
            return converter.xlsx_to_pdf()
        if format_upper == 'CSV':
            return converter.xlsx_to_csv()
        if format_upper == 'TXT':
            return converter.xlsx_to_txt()

    if file_ext == 'pptx':
        if format_upper == 'PDF':
            return converter.pptx_to_pdf()
        if format_upper == 'TXT':
            return converter.pptx_to_txt()

    if file_ext == 'txt':
        if format_upper == 'PDF':
            return converter.txt_to_pdf()
        if format_upper == 'DOCX':
            return converter.txt_to_docx()

    if file_ext == 'csv':
        if format_upper == 'XLSX':
            return converter.csv_to_xlsx()
        if format_upper == 'TXT':
            return converter.csv_to_txt()

    return None, f"Conversão {file_ext.upper()} → {format_upper} não suportada"


@conversion_bp.route('/convert', methods=['POST'])
def convert_file():
    """Endpoint universal de conversão de arquivos."""

    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    if 'formats' not in request.form:
        return jsonify({'error': 'Nenhum formato selecionado'}), 400

    file = request.files['file']
    formats = request.form.getlist('formats')

    if not formats:
        return jsonify({'error': 'Nenhum formato selecionado'}), 400

    # Salvar arquivo (validação interna)
    filepath, msg = save_upload(file)
    if not filepath:
        return jsonify({'error': msg}), 400

    file_ext = get_file_extension(filepath)
    allowed = SUPPORTED_CONVERSIONS.get(file_ext, [])

    # Validar formatos solicitados contra o tipo do arquivo
    invalid = [f for f in formats if f.upper() not in allowed]
    if invalid:
        remove_file(filepath)
        return jsonify({'error': f'Formatos inválidos para .{file_ext}: {invalid}'}), 400

    output_dir = create_output_dir()

    try:
        output_files = []
        errors = []

        for fmt in formats:
            files, error = _run_conversion(filepath, file_ext, fmt.upper())
            if error:
                errors.append(f"{fmt.upper()}: {error}")
            elif files:
                output_files.extend(files)

        remove_file(filepath)

        if not output_files:
            return jsonify({'error': 'Falha na conversão: ' + ' | '.join(errors)}), 500

        # Arquivo único → retornar direto
        if len(output_files) == 1:
            fp = output_files[0]
            return send_file(fp, as_attachment=True, download_name=os.path.basename(fp))

        # Múltiplos arquivos → ZIP
        zip_filename = f"{Path(filepath).stem}_converted.zip"
        zip_path = os.path.join(output_dir, zip_filename)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for fp in output_files:
                zipf.write(fp, arcname=os.path.basename(fp))
        for fp in output_files:
            remove_file(fp)

        return send_file(zip_path, as_attachment=True, download_name=zip_filename)

    except Exception as e:
        print(f"ERRO GERAL NA CONVERSÃO: {str(e)}")
        print(traceback.format_exc())
        remove_file(filepath)
        return jsonify({'error': f'Erro no servidor: {str(e)}'}), 500


@conversion_bp.route('/formats', methods=['GET'])
def get_formats():
    """Retorna formatos de saída disponíveis por tipo de arquivo."""
    return jsonify(SUPPORTED_CONVERSIONS), 200


@conversion_bp.route('/health', methods=['GET'])
def health_check():
    """Verificar saúde da API."""
    return jsonify({'status': 'ok'}), 200
