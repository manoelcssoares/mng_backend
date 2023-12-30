# import mysql.connector
# from mysql.connector import Error

# def get_db_connection():
#     try:
#         connection = mysql.connector.connect(
#             host = "localhost",
#             database = "mng_backend",
#             user = "mng_user",
#             password = "2)KA=P2ir4"
#         )
#         if connection.is_connected():
#             return connection
#     except Error as e:
#         print("Erro ao conectar ao MySQL", e)

import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            database = "mng_db",
            user = "mng_user",
            password = "2)KA=P2ir4#$%*"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Erro ao conectar ao MySQL", e)