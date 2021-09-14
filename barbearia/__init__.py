from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from requests import Request


app = Flask(__name__)
app.config['SECRET_KEY'] = '03c67c676b4fcf005bee69ae'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://nawtnucbclasnz:3011841ec78eb8824ffa194f91af7e3b8ebdfce225518de9a7161190186ddf3c@ec2-44-195-201-3.compute-1.amazonaws.com:5432/d26chn0b080oo9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
request = Request(app)

from barbearia import routes