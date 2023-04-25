from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Pessoa(db.Model):

    __tablename__ = 'pessoa'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    email = db.Column(db.String)
    cpf = db.Column(db.String)
    endereco = db.Column(db.String)

    def _init_(self, nome, telefone, email, cpf, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco


db.create_all()


@app.route("/index")
def index():
    return render_template("index.html")


if __name__ = '__main__':
    app.run(debug=True)
