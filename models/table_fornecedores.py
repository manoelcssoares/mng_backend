import db.database_connection as database_connection

def create_fornecedores_table():

# Crie uma conexão usando a função definida em database_connection.py
    connection = database_connection.create_connection()

    # Crie um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Defina a consulta SQL para criar a tabela com várias colunas
    create_table_query = """
    CREATE TABLE IF NOT EXISTS tbl_emp (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        razao_social VARCHAR(255),
        email VARCHAR(255),
        cnpj VARCHAR(18) NOT NULL,
        cep VARCHAR(9),
        endereco VARCHAR(255),
        bairro VARCHAR(255),
        estado VARCHAR(2),
        numero VARCHAR(10),
        complemento VARCHAR(255),
        cidade VARCHAR(255),
        tipo ENUM('material_de_construcao', 'material_de_pintura', 'material_eletrico', 'material_hidraulico'),
        contato VARCHAR(255),
        site VARCHAR(255),
        celular VARCHAR(15)
)
"""

    # Execute a consulta SQL para criar a tabela
    cursor.execute(create_table_query)

    # Commit as alterações e feche o cursor e a conexão
    connection.commit()
    cursor.close()
    connection.close()
