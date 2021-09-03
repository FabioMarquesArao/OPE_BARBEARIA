from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length


class RegisterForm(FlaskForm):
    username = StringField(label='Nome:', validators=[DataRequired(), Length(min=2, max=30)])
    cpf = StringField(label='CPF:', validators=[DataRequired(), Length(11)])
    telefone = StringField(label='Telefone:', validators=[DataRequired(), Length(11)])
    email = StringField(label='Email:', validators=[DataRequired(), Email()])
    senha = PasswordField(label='Senha:', validators=[DataRequired(), Length(min=6)])
    confirmaSenha = PasswordField(label='Confirme a Senha:', validators=[EqualTo('senha')])
    submit = SubmitField(label='Criar Conta')
    data_nascimento = StringField(label='Data de Nascimento:', validators=[DataRequired(), Length(max=14)])



