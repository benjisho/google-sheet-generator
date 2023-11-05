# backend/app/__init__.py
import logging
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=['http://95.179.202.222:3000'])  # Update this line

    # Set up basic logging configuration
    logging.basicConfig(level=logging.DEBUG)

    from .routes import main  # Importing routes
    app.register_blueprint(main)

    return app
