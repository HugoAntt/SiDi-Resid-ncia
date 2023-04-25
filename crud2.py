from flask import Flask

app = Flask(__name__)


@app.route("/")
def crudApp():
    return "<h1> Tome app funcionando<h1>"


if __name__ == "__main__":
    app.run()
