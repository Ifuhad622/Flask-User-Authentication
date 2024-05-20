from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy importSQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes
