from barbearia import db

class Barbeiro(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nome = db.Column(db.String(length=50), nullable=False)