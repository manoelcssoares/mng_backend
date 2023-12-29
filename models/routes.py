import pymysql
from app import app
from config import mysql
from flask import jsonify, request

def get_db_connection():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

# def close_db_connection(conn, cursor):
#     cursor.close()
#     conn.close()

def safe_close_db_connection(conn, cursor):
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()


@app.route('/create', methods=['POST'])
def create_user():
    conn, cursor = None, None
    try:
        json = request.json
        if json is not None:
            name = json.get('name')
            email = json.get('email')
            phone = json.get('phone')
            address = json.get('address')
        if name and email and phone and address:
            conn, cursor = get_db_connection()
            sqlQuery = "INSERT INTO user(name, email, phone, address) VALUES(%s, %s, %s, %s)"
            bindData = (name, email, phone, address)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('User added successfully!')
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        safe_close_db_connection(conn, cursor)

@app.route('/user/<int:user_id>')
def user_details(user_id):
    conn, cursor = None, None
    try:
        conn, cursor = get_db_connection()
        cursor.execute("SELECT id, name, email, phone, address FROM user WHERE id = %s", (user_id,))
        userRow = cursor.fetchone()
        if userRow:
            response = jsonify(userRow)
            response.status_code = 200
            return response
        else:
            return show_message()
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        safe_close_db_connection(conn, cursor)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn, cursor = None, None
    try:
        conn, cursor = get_db_connection()
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        conn.commit()
        response = jsonify('User deleted successfully!')
        response.status_code = 200
        return response
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        safe_close_db_connection(conn, cursor)

@app.route('/user', methods=['GET'])
def get_all_users():
    conn, cursor = None, None
    try:
        conn, cursor = get_db_connection()
        cursor.execute("SELECT id, name, email, phone, address FROM user")
        users = cursor.fetchall()
        response = jsonify(users)
        response.status_code = 200
        return response
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        safe_close_db_connection(conn, cursor)


@app.errorhandler(404)
def show_message(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response
