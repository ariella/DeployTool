#!/usr/bin/python


from flask import Blueprint, jsonify,request
from Models.APIModel import grupos as GruposModel
import json

grupo_bp = Blueprint('grupos',__name__)


@grupo_bp.route("/grupos/")
def listar_grupos():
    todos = GruposModel.objects().to_json()
    retorno = {"grupos":json.loads(todos)}
    return jsonify(retorno)
    

@grupo_bp.route("/grupos/<id>",methods=["POST"])
def adicionar_integrante_grupo():
    g = GruposModel.object(id==id).first()
    novo = request.get_json()
    g.integrantes.append(novo.get("nome"))
    g.save()

    retorno={"message":"Usuario cadastrado com sucesso"}
    return jsonify(retorno)


@grupo_bp.route("/grupos/",methods=["POST"])
def cadastrar_grupos():
    novo = request.get_json()
    g = GruposModel()
    g.nome = novo.get("nome")
    g.save()

    retorno={"message":"Grupo cadastrado com sucesso"}
    return jsonify(retorno)


@grupo_bp.route("/grupos/<id>/",methods=["PUT"])
def atualizar_grupos(id):
    g = GruposModel.objects(id=id).first()   
    dados = request.get_json()
    g.nome=dados.get("nome")
    
    g.email = dados.get("email")
    g.save()
    retorno={"message":"Usuario atualizado com sucesso"}
    return jsonify(retorno)


@grupo_bp.route("/grupos/<id>/",methods=["DELETE"])
def remover_grupos(id):
    u = GruposModel.objects(id=id).first()   
    u.delete() 
    retorno={"message":"Grupo removido com sucesso"}
    return jsonify(retorno)


if __name__ == '__main__':
    grupo_bp.run(port=8000,debug=True)
