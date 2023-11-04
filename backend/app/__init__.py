from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enables CORS for all routes

    from .routes import main  # Importing routes
    app.register_blueprint(main)

    return app
