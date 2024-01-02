class Fornecedor:
    CREATE_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS fornecedores (
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

class Usuario:
    CREATE_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        senha VARCHAR(100) NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

class Produto:
    CREATE_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS produtos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        descricao TEXT,
        preco DECIMAL(10, 2) NOT NULL,
        estoque INT NOT NULL
    )
    """

class Compra:
    # SQL para criar a tabela de compras
    CREATE_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS compras (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_usuario INT,
        id_produto INT,
        quantidade INT,
        data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
        FOREIGN KEY (id_produto) REFERENCES produtos(id)
    )
    """