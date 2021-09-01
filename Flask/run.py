from barbearia import app
from flask_sqlalchemy import SQLAlchemy



if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://fnlwdzmflpxpby:10500a639e7edb5a403284b9334bbbea6f287d16c33646ef901e2d1cd6b14a64@ec2-34-194-14-176.compute-1.amazonaws.com:5432/daq0i5hffjvjft'

db = SQLAlchemy(app)

class Cadastrousuario(db.Model):
    __tablename__ = "usuarioscadastrados"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    senha = db.Column(db.String(50))
    email = db.Column(db.String(50))
    cpf = db.Column(db.String(50))
    telefone = db.Column(db.String(15))
    datanascimento = db.Column(db.String(10))

    def __init__(self, nome, senha, email, cpf, telefone, datanascimento):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.datanascimento = datanascimento

db.create_all()

