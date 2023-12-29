from flask import request
import MySQLdb
from config import connect_to_mysql
from app import app

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    db = connect_to_mysql
    cursor = db.cursor()
    try:
        cursor.execute('INSERT INTO user (name, email, phone, address) VALUES (%s, %s, %s, %s)', (name, email, phone, address))
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return str(e)
    finally:
        cursor.close()
        db.close

    return 'usuario criado com sucesso!'