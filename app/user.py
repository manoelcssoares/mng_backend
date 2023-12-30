from app import app
from flask import jsonify

@app.route('/')
def home():
    return "Bem-vindo à minha API Flask!"

@app.route('/api/data')
def get_data():
    
    return jsonify(data)
