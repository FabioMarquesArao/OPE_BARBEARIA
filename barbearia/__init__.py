from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from requests import Request
from barbearia.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message = "Você deve estar logado para acessar está página"
login_manager.login_message_category = "danger"
request = Request(app)

from barbearia.auth import auth_bp
app.register_blueprint(auth_bp)

from barbearia.main import main_bp
app.register_blueprint(main_bp)

from barbearia.agendamento import agendamento_bp
app.register_blueprint(agendamento_bp)

with app.app_context():
    db.create_all()