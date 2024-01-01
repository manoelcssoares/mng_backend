# Exemplo de create_tables.py

from app.db import get_db_connection
from app.models import Tbl_Supplier, Tbl_User
from mysql.connector import Error

def create_tables():
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(Tbl_Supplier.create_tbl_supplier)
            cursor.execute(Tbl_User.create_tbl_user)
            conn.commit()
            print("Tabelas criadas com sucesso.")
        except Error as e:
            print(f"Erro ao criar tabelas: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

if __name__ == '__main__':
    create_tables()
