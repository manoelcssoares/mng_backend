from flask import Flask
from .routes.user import init_routes
from .routes.supplier import init_routes

def create_app():
    app = Flask(__name__)

    init_routes(app)

    return app
