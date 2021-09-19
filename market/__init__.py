# Initialization for Flask Market
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initializing Flask App as app
app = Flask(__name__)
# Adding DATABASE_URI and SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '743d241d15d7d43176cbd7fd'
# Initializing SQL Database as db
db = SQLAlchemy(app)
# Initializing Bcrypt and LoginManager
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import routes
