from flask import Flask
from models.table_user import create_user_table
from models.table_fornecedores import create_fornecedores_table
from routes import user

create_user_table()
create_fornecedores_table()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)