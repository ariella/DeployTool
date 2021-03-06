#!/usr/bin/python

from flask import Flask, jsonify
from blueprints.Usuarios import usuario_bp
from blueprints.Grupos import grupo_bp

app = Flask(__name__)
app.register_blueprint(usuario_bp)
app.register_blueprint(grupo_bp)

@app.route("/")
def index():
    resposta = {"message":"aplicacao em Flask"}
    return jsonify(resposta)


if __name__ == '__main__':
    app.run(port=8000,debug=True)
