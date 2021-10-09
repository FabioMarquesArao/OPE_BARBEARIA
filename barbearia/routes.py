from flask_login.utils import login_required
from barbearia import app
from flask import render_template, redirect, url_for, flash
from barbearia.forms import RegisterForm, LoginForm
from barbearia.models import Usuario
from barbearia import db
from barbearia.email_sender import email_cadastro
from flask_login import login_user, logout_user



db.create_all()

@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro_page():
    form = RegisterForm()
    if form.validate_on_submit():
        novo_usuario = Usuario(username=form.username.data, password=form.senha.data,
                               email=form.email.data, cpf=form.cpf.data,
                               telefone=form.telefone.data, data_nascimento=form.data_nascimento.data)
        db.session.add(novo_usuario)
        db.session.commit()
        email_cadastro(novo_usuario.username,novo_usuario.email)
        login_user(novo_usuario)
        flash(f'Conta criada com sucesso! Você está logado como: {novo_usuario.username}', category='success')
        return redirect(url_for("home_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Aconteceu um erro durante o cadastro: {err_msg}', category='danger')
    return render_template('cadastro.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Usuario.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.senha.data):
            login_user(attempted_user)
            flash(f'Você está logado como: {attempted_user.email}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Nome de usuário ou senha incorretos. Tente novamente.', category='danger')
    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Você foi desconectado", category="info")
    return redirect(url_for("home_page"))

@app.route("/agendamento")
@login_required
def agendamento_page():
    return render_template("calendar.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")
