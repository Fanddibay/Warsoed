from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#Konfigurasi dasar aplikasi
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Login menyusul

app.config['SECRET_KEY'] = 'd18596dc242fc3ff4e18e842a7ad7072'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgreunsoed@localhost:5432/warsoed'

import warsoed.routes