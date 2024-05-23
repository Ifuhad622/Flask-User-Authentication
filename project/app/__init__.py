#!/usr/bin/env python3

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import routes at the end to avoid circular imports


def register_routes():
    from app import routes


register_routes()
