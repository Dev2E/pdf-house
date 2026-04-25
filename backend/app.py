import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.conversion import conversion_bp
from utils.file_handler import cleanup_temp, ensure_temp_dir

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurar CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Registrar blueprints
app.register_blueprint(conversion_bp)

# Inicializar diretórios
ensure_temp_dir()

# Rotas básicas
@app.route('/', methods=['GET'])
def index():
    return {
        'message': 'PDF Converter API',
        'version': '2.0.0',
        'engine': 'pymupdf',
        'endpoints': {
            'convert': 'POST /api/convert',
            'health': 'GET /api/health'
        }
    }, 200

@app.before_request
def before_request():
    """Executar antes de cada request."""
    cleanup_temp()

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(debug=True, port=port)
