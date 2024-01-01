class Tbl_Supplier:
    create_tbl_supplier = """
    CREATE TABLE IF NOT EXISTS tbl_supplier (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        razao_social VARCHAR(255) NOT NULL,
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
        site VARCHAR(255),
        celular VARCHAR(15)
)
"""

class Tbl_User:
    create_tbl_user = """
    CREATE TABLE IF NOT EXISTS tbl_user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        senha VARCHAR(100) NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""