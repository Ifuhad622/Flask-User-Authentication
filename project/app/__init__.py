#!/usr/bin/env python3

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import Config

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

# Import routes, models, and forms
from app import routes, models, forms

# Import routes at the end to avoid circular imports
def register_routes():
    from app import routes

register_routes()

# Create database tables if they do not exist
with app.app_context():
    db.create_all()
