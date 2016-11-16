#!/usr/bin/python

import requests
import json

def listar():
    response = requests.get("http://localhost:5000/usuarios/")
    response = json.loads(response.content)

    for u in response.get("usuarios"):
        print u.get("id"),u.get("nome"),u.get("email")

def atualizar():
    uid = raw_input("Entre com o id que deseja atualizar: ")
    novo={}
    novo["nome"] = raw_input("Digite o novo nome:")
    novo["email"] = raw_input("Digite o novo e-mail: ")

    content_type ={"Content-Type":"application/json"}
    response = requests.put("http://localhost:5000/usuarios/{0}/".format(uid),
                        headers=content_type,data=json.dumps(novo))
    print response.content

def cadastrar(linha):
    novo={}
    novo["nome"] = linha.replace("\n","")
    novo["email"] = novo.get("nome").replace(" ",".").lower()+"@dexter.com.br"

    content_type ={"Content-Type":"application/json"}
    response = requests.post("http://localhost:5000/usuarios/",
                        headers=content_type,data=json.dumps(novo))
    print response.content


def deletar():
    listar()
    uid = raw_input("Entre com o id para deletar: ")

    content_type ={"Content-Type":"application/json"}
    response = requests.delete("http://localhost:5000/usuarios/{0}/".format(uid),
                        headers=content_type)
    print response.content


if __name__ == '__main__':
#    cadastrar()
#    deletar()

      with open("usuarios.txt","r") as f:
        for l in f.readlines():
            cadastrar(l)





