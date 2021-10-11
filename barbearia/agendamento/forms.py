from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Length


class AgendamentoForm(FlaskForm):
    titulo = SelectField(label='Selecione o Serviço', choices=["Corte Simples", "Corte + Barba", "Seladinho", "Qímica"], validators=[DataRequired()])
    barbeiro = SelectField(label="Selecione o Barbeiro", choices=["Barbeiro 1", "Barbeiro 2", "Carlos"], validators=[DataRequired()])
    start_atend = StringField(label="Início do atendimento", validators=[DataRequired()])
    end_atend = StringField(label="Fim do atendimento", validators=[DataRequired()])
    submit = SubmitField(label="Agendar")
