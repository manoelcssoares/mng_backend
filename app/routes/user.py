from flask import request, jsonify
from ..db import get_db_connection
from mysql.connector import Error

def init_routes(app):

    @app.route('/user', methods=['POST'])
    def create_user():
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO tbl_user (nome, email, senha) VALUES (%s, %s, %s)",
                           (data['nome'], data['email'], data['senha']))
            conn.commit()
            return jsonify({"status": "Usuário criado com sucesso"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route('/user', methods=['GET'])
    def read_user():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM tbl_user")
            user = cursor.fetchall()
            return jsonify(user)
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route('/user/<int:id>', methods=['PUT'])
    def update_user(id):
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE tbl_user SET nome = %s, email = %s, senha = %s WHERE id = %s",
                           (data['nome'], data['email'], data['senha'], id))
            conn.commit()
            return jsonify({"status": "Usuário atualizado com sucesso"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM tbl_user WHERE id = %s", (id,))
            conn.commit()
            return jsonify({"status": "Usuário deletado com sucesso"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
