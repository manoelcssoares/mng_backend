from app import app
from models.routes import *
from models.user import add_user

        
if __name__ == "__main__":
    app.run(debug=True)