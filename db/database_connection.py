import mysql.connector

# Replace these with your database credentials
host = "localhost"
user = "mng_user"
password = "2)KA=P2ir4"
database = "mng_backend"

def create_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
)