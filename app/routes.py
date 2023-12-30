from flask import jsonify
from .db import get_db_connection


def init_routes(app):
    @app.route('/')
    def home():
        return "Bem-vindo à minha API Flask!"

    @app.route('/data')
    def get_data():
        conn = get_db_connection()
        if conn is not None:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tbl_user")
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return jsonify(data)
        else:
            return jsonify({"error": "Erro na conexão com o banco de dados"}), 500