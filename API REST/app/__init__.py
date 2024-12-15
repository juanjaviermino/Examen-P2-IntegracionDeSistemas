from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the database
    DB_CONFIG = {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT")
    }

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app
