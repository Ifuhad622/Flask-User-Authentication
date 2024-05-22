from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '91907741'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

# Initialize database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Importing models and views
from models import User

if __name__ == "__main__":
    app.run(debug=True)
