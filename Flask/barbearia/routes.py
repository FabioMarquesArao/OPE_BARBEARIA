from barbearia import app
from flask import render_template

@app.route('/')
def menu_page():
    return render_template('index.html')

@app.route('/home')
def home_page():
    return render_template('menu.html')
