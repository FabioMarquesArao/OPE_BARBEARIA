from barbearia import db

class Usuario(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    cpf = db.Column(db.String(length=11), nullable=False)
    telefone = db.Column(db.String(length=11), nullable=False)
    dataNascimento = db.Column(db.String(length=14), nullable=False)  


    def __repr__(self):
        return f'User {self.username}'



