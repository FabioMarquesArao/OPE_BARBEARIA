from barbearia import app
from flask import render_template, request, redirect, url_for

from Flask.run import Cadastrousuario
from Flask.run import db


@app.route('/')
def menu_page():
    return render_template('index.html')

@app.route('/home')
def home_page():
    return render_template('menu.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrousuario', methods=['GET', 'POST'])
def cadastrousuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        datanascimento = request.form.get('datanascimento')
        if nome:
            f = Cadastrousuario(nome, senha, email, cpf, telefone, datanascimento)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for('menu_page'))