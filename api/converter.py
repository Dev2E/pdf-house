"""
Vercel Serverless Function - PDF Converter API
"""
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../backend'))

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from backend.routes.conversion import conversion_bp

# Create Flask app
app = Flask(__name__)
CORS(app)

# Register conversion blueprint
app.register_blueprint(conversion_bp, url_prefix='/api')

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})

@app.route('/api')
def api_index():
    return jsonify({
        'name': 'PDF Pro API',
        'version': '1.0.0',
        'endpoints': ['/api/convert', '/api/health']
    })

# Handler for Vercel
def handler(request):
    """Vercel serverless function handler"""
    return app(request)
