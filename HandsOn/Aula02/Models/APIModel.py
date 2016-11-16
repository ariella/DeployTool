#!/usr/bin/python

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from datetime import datetime

app= Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db":"dexter-api"}

db = MongoEngine(app)


class Usuarios(db.Document):
    nome  = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(default=datetime.now())

class grupos(db.Document):
    nome = db.StringField(unique=True)
    integrantes = db.ListField()


if __name__ == '__main__':
    pass
#    criar novo usuario
#    novo = db.Usuarios()
#    novo.nome ="nome"
#    novo.email = "email"
#    novo.save()
#    update => busca antes e depois .save

#    listar todos
#    usuarios = Usuarios.objects() 
#    for u in usuarios:  
#        print u.to_json()

#    buscar 1
#    usuarios = Usuarios.objects(email="alisson.machado@4linux.com.br").first()   

#    deleter usuario
#    primeiro busca => usuarios = Usuarios.objects(email="alisson.machado@4linux.com.br").first()   
#    usuarios.delete() 








