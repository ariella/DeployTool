#!/usr/bin/python

from flask import Blueprint, jsonify,request
from flask.ext.mongoengine import MongoEngine
from Models.APIModel import Usuarios as UsuariosModel
import json

usuario_bp = Blueprint('usuarios',__name__)


@usuario_bp.route("/usuarios/")
def listar_usuarios():
    todos = UsuariosModel.objects().to_json()
    retorno = {"usuarios":json.loads(todos)}
    return jsonify(retorno)
    

@usuario_bp.route("/usuarios/",methods=["POST"])
def cadastrar_usuarios():
    novo = request.get_json()
    u = UsuariosModel()
    u.nome = novo.get("nome")
    u.email = novo.get("email")
    u.save()

    retorno={"message":"Usuario cadastrado com sucesso"}
    return jsonify(retorno)


@usuario_bp.route("/usuarios/<id>/",methods=["PUT"])
def atualizar_usuarios(id):
    u = UsuariosModel.objects(id=id).first()   
    dados = request.get_json()
    u.nome=dados.get("nome")
    u.email = dados.get("email")
    u.save()
    retorno={"message":"Usuario atualizado com sucesso"}
    return jsonify(retorno)


@usuario_bp.route("/usuarios/<id>/",methods=["DELETE"])
def remover_usuarios(id):
    u = UsuariosModel.objects(id=id).first()   
    u.delete() 
    retorno={"message":"Usuario removidocom sucesso"}
    return jsonify(retorno)


if __name__ == '__main__':
    usuario_bp.run(port=8000,debug=True)
