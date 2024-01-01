from flask import request, jsonify
from ..db import get_db_connection
from mysql.connector import Error

def init_routes(app):

    @app.route('/supplier', methods=['POST'])
    def create_supplier():
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO tbl_supplier (nome, razao_social, email, cnpj, cep, endereco, bairro, estado, numero, complemento, cidade, tipo, site, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (data['nome'], data['razao_social'], data['email'], data['cnpj'], data['cep'], data['endereco'], data['bairro'], data['estado'], data['numero'], data['complemento'], data['cidade'], data['tipo'], data['site'], data['celular']))
            conn.commit()
            return jsonify({"status": "Fornecedor cadastrado com sucesso"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route('/supplier', methods=['GET'])
    def read_supplier():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM tbl_supplier")
            supplier = cursor.fetchall()
            return jsonify(supplier)
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route('/supplier/<int:id>', methods=['PUT'])
    def update_supplier(id):
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE tbl_supplier SET nome = %s, razao_social = %s, email = %s, cnpj = %s, cep = %s, endereco = %s, bairro = %s, estado = %s, numero = %s, complemento = %s, cidade = %s, tipo = %s, site = %s, celular = %s  WHERE id = %s",
                           (data['nome'], data['razao_social'], data['email'], data['cnpj'], data['cep'], data['endereco'], data['bairro'], data['estado'], data['numero'], data['complemento'], data['cidade'], data['tipo'], data['site'], data['celular'], id))
            conn.commit()
            return jsonify({"status": "Fornecedor atualizado com sucesso"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

    @app.route('/supplier/<int:id>', methods=['DELETE'])
    def delete_supplier(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM tbl_supplier WHERE id = %s", (id,))
            conn.commit()
            return jsonify({"status": "Fornecedor deletado com sucesso"}), 200
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
