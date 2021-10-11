from flask.json import jsonify
from flask_login.utils import login_required
from flask import render_template, redirect, url_for, flash, request
from barbearia.models import Agendamento
from barbearia.agendamento import agendamento_bp
from barbearia.agendamento.forms import AgendamentoForm




# Incio agendamento routes
@agendamento_bp.route("/agendamento", methods=["GET", "POST"])
@login_required
def agendamento_page():
    form = AgendamentoForm()
    agendamentos = Agendamento.query.all()
    return render_template("calendar.html", agendamentos=agendamentos, form=form)
