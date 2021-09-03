from barbearia import app
from flask import render_template, redirect, url_for
from barbearia.forms import RegisterForm
from barbearia.models import Usuario
from barbearia import db

@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro_page():
    form = RegisterForm()
    if form.validate_on_submit():
        novo_usuario = Usuario(username=form.username.data, password_hash=form.senha.data,
                               email=form.email.data, cpf=form.cpf.data,
                               telefone=form.telefone.data, dataNascimento=form.dataNascimento.data)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for("home_page"))
    if form.errors != {}:
        print(form.errors)
    return render_template('cadastro.html', form=form)