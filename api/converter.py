"""
Vercel Serverless Function - PDF Converter API
"""
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../backend'))

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.routes.conversion import conversion_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(conversion_bp, url_prefix='/')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

