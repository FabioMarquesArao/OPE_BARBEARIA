from barbearia import db

class Agendamento(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    start_atend = db.Column(db.TIMESTAMP(), nullable=False, unique=True)
    end_atend = db.Column(db.TIMESTAMP(), nullable=False, unique=True)
    title = db.Column(db.String(length=150), nullable=False)