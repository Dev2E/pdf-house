"""
PDF Pro - Aplicação Full-Stack
Serve frontend estático + API backend em uma única app Flask
"""
import os
import sys
from pathlib import Path
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

# Adicionar backend ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Importar routes do backend
from backend.routes.conversion import conversion_bp

# Criar app Flask
app = Flask(__name__, static_folder='frontend/dist', static_url_path='')

# Ativar CORS
CORS(app)

# Registrar blueprint da API
app.register_blueprint(conversion_bp, url_prefix='/api')

# Servir frontend estático
@app.route('/')
def serve_index():
    """Serve index.html para SPA (Single Page Application)"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve arquivos estáticos (CSS, JS, etc)"""
    file_path = os.path.join(app.static_folder, path)
    
    # Se é um arquivo que existe, serve
    if os.path.isfile(file_path):
        return send_from_directory(app.static_folder, path)
    
    # Se não existe, retorna index.html (para rotas da SPA)
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})

@app.errorhandler(404)
def not_found(error):
    """Serve index.html para rotas não encontradas (SPA routing)"""
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
