import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    DEBUG = True  # Set to False in production
