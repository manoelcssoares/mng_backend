import db.database_connection as database_connection

def create_user_table():

# Crie uma conexão usando a função definida em database_connection.py
    connection = database_connection.create_connection()

    # Crie um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Defina a consulta SQL para criar a tabela com várias colunas
    create_table_query = """
    CREATE TABLE IF NOT EXISTS tbl_user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        idade INT,
        email VARCHAR(255),
        cidade VARCHAR(255)
    )
    """

    # Execute a consulta SQL para criar a tabela
    cursor.execute(create_table_query)

    # Commit as alterações e feche o cursor e a conexão
    connection.commit()
    cursor.close()
    connection.close()
