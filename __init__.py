from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from dotenv import load_dotenv

import os

load_dotenv()

WEBSITE_NAME = os.getenv("WEBSITE_NAME")
DATABASE_URI = os.getenv("DATABASE_URI")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mB(!Gn#T#T>7K.FN~2=V9oW<2Y#[.3'
app.config['MONGO_URI'] = DATABASE_URI
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
db = PyMongo(app).db
bcrypt = Bcrypt(app)

from .views import views
from .auth import auth
from .items import items

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(items, url_prefix='/')
