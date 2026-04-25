import os
import io
from pathlib import Path
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
from docx import Document
from docx.shared import Pt
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

class PDFConverter:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pdf_filename = Path(pdf_path).stem
    
    def to_images(self, format='PNG', dpi=150):
        """Converte PDF para imagens (PNG ou JPG)."""
        try:
            images = convert_from_path(self.pdf_path, dpi=dpi)
            output_files = []
            
            for i, image in enumerate(images):
                output_filename = f"{self.pdf_filename}_page_{i+1:03d}.{format.lower()}"
                output_path = os.path.join('./temp/output', output_filename)
                
                if format.upper() == 'JPG':
                    # Converter para RGB para JPG (sem transparência)
                    if image.mode in ('RGBA', 'LA'):
                        # Criar imagem branca como fundo
                        background = Image.new('RGB', image.size, (255, 255, 255))
                        # Extrair canal alpha e fazer composite
                        alpha = image.split()[-1]
                        background.paste(image.convert('RGB'), mask=alpha)
                        background.save(output_path, 'JPEG', quality=95)
                    else:
                        # Converter para RGB se não estiver
                        rgb_image = image.convert('RGB') if image.mode != 'RGB' else image
                        rgb_image.save(output_path, 'JPEG', quality=95)
                else:
                    image.save(output_path, 'PNG')
                
                output_files.append(output_path)
            
            return output_files, None
        except Exception as e:
            return None, f"Erro ao converter para imagens: {str(e)}"
    
    def to_text(self):
        """Converte PDF para TXT."""
        try:
            text = ""
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    extracted = page.extract_text()
                    text += extracted + "\n"
            
            output_filename = f"{self.pdf_filename}.txt"
            output_path = os.path.join('./temp/output', output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            
            return [output_path], None
        except Exception as e:
            return None, f"Erro ao converter para TXT: {str(e)}"
    
    def to_docx(self):
        """Converte PDF para DOCX."""
        try:
            doc = Document()
            
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    text = page.extract_text()
                    if page_num > 1:
                        doc.add_page_break()
                    doc.add_paragraph(text)
            
            output_filename = f"{self.pdf_filename}.docx"
            output_path = os.path.join('./temp/output', output_filename)
            doc.save(output_path)
            
            return [output_path], None
        except Exception as e:
            return None, f"Erro ao converter para DOCX: {str(e)}"
    
    def to_xlsx(self):
        """Converte PDF para XLSX."""
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "PDF Data"
            
            row = 1
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    text = page.extract_text()
                    lines = text.split('\n')
                    
                    for line in lines:
                        if line.strip():
                            ws[f'A{row}'] = line
                            row += 1
            
            output_filename = f"{self.pdf_filename}.xlsx"
            output_path = os.path.join('./temp/output', output_filename)
            wb.save(output_path)
            
            return [output_path], None
        except Exception as e:
            return None, f"Erro ao converter para XLSX: {str(e)}"
