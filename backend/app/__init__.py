# backend/app/__init__.py
import logging
from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

def create_app():
    app = Flask(__name__)
    # Adjust the origins to allow requests from the specific frontend origin
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Set up basic logging configuration
    logging.basicConfig(level=logging.DEBUG)

    from .routes import main  # Importing routes
    app.register_blueprint(main)

    scheduler = BackgroundScheduler()
    scheduler.start()

    app.config['SCHEDULER'] = scheduler

    return app
