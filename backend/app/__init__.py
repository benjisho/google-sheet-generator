# backend/app/__init__.py
import logging
from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/generate-sheet": {"origins": "http://95.179.193.18:3000"}})

    # Set up basic logging configuration
    logging.basicConfig(level=logging.DEBUG)

    from .routes import main  # Importing routes
    app.register_blueprint(main)

    scheduler = BackgroundScheduler()
    scheduler.start()

    app.config['SCHEDULER'] = scheduler

    return app
