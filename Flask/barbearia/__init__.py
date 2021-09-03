from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '03c67c676b4fcf005bee69ae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barbearia.db'
db = SQLAlchemy(app)


from barbearia import routes