import os
from pathlib import Path
from PIL import Image


class ImageConverter:
    SUPPORTED_INPUTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp'}
    SUPPORTED_OUTPUTS = ['PDF', 'PNG', 'JPG', 'WEBP']

    def __init__(self, file_path):
        self.file_path = file_path
        self.filename_stem = Path(file_path).stem
        self.output_dir = self._get_output_dir()

    def _get_output_dir(self):
        output_dir = os.path.join(os.path.dirname(self.file_path), '..', 'output')
        output_dir = os.path.abspath(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    def to_pdf(self):
        """Converte imagem para PDF."""
        try:
            img = Image.open(self.file_path)
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            elif img.mode != 'RGB':
                img = img.convert('RGB')

            output_path = os.path.join(self.output_dir, f"{self.filename_stem}.pdf")
            img.save(output_path, 'PDF', resolution=150)
            return [output_path], None
        except Exception as e:
            return None, f"Erro ao converter para PDF: {str(e)}"

    def to_image(self, format='PNG'):
        """Converte entre formatos de imagem (PNG, JPG, WEBP)."""
        try:
            img = Image.open(self.file_path)
            fmt = format.upper()

            if fmt in ('JPG', 'JPEG'):
                ext = 'jpg'
                pil_format = 'JPEG'
                if img.mode in ('RGBA', 'P', 'LA'):
                    img = img.convert('RGB')
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
            elif fmt == 'WEBP':
                ext = 'webp'
                pil_format = 'WEBP'
            else:
                ext = 'png'
                pil_format = 'PNG'

            output_path = os.path.join(self.output_dir, f"{self.filename_stem}.{ext}")
            img.save(output_path, pil_format)
            return [output_path], None
        except Exception as e:
            return None, f"Erro ao converter para {format}: {str(e)}"
