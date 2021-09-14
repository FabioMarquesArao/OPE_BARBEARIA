from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from requests import Request


app = Flask(__name__)
app.config['SECRET_KEY'] = '03c67c676b4fcf005bee69ae'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://fnlwdzmflpxpby:10500a639e7edb5a403284b9334bbbea6f287d16c33646ef901e2d1cd6b14a64@ec2-34-194-14-176.compute-1.amazonaws.com:5432/daq0i5hffjvjft'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
request = Request(app)

from barbearia import routes