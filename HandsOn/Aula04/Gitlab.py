#!/usr/bin/python

import requests
import json

class Gitlab():
    def __init__(self):
        self.token="y5BAhu9Tdmi84XjSY2yR"
        self.servidor = "192.168.0.3"
        self.headers = {"Content-Type":"application/json"}

    def _post(self,recurso,data):
        response = requests.post("http://{0}/api/v3/{1}?private_token={2}"
                                    .format(self.servidor,recurso,self.token)
                                    ,data=json.dumps(data),headers=self.headers)
        return response

    def _get(self,recurso):
#        response = requests.get("http://{0}/api/v3/{1}?private_token={2}"
#                                    .format(self.servidor,recurso,self.token)
#                                    ,data=json.dumps(data),headers=self.headers)  

        response = requests.get("http://{0}/api/v3/{1}?private_token={2}"
                                    .format(self.servidor,recurso,self.token)
                                    ,headers=self.headers)          
        
        return response

    def criar_usuario(self):
        recurso = "users"
        data = {"username":"teste5","email":"teste5@teste5.com","name":"Teste05","password":"4linux1234"}
        response = self._post(recurso,data)
        if response.status_code == 201:
            print "Usuario criado com sucesso"
        else:
            print "Falhou ao criar usuario", response.content

    def criar_projeto(self):
        recurso = "projects"
        data = {"name":"Projeto Aula02"}
        response = self._post(recurso,data)
        if response.status_code == 201:
            print "Projeto criado com sucesso"
        else:
            print "Falhou ao criar projeto", response.content
    
    def adicionar_webhook(self,nome,url):
        projetos = self.listar_projetos()
        projeto = [p for p in projetos if p.get("name") == nome]
       
        if projeto:
            pid = projeto[0].get("id")
            recurso = "projects/%s/hooks"%pid
            data = {"name":nome, "url":url}
            response = self._post(recurso,data)
            if reponse.status_code == 201:
                print "Webhook criado com sucesso"
            else:
                print "Falhou ao cadastrar: ", response.content
        else:
            print "Projeto nao encontrado"

    def adicionar_desenvolvedor(self,nome,email):
        projetos = self.listar_projetos()
        projeto = [p for p in projetos if p.get("name") == nome]
        
        usuarios = self.listar_usuarios()
        usuario = [u for u in usuarios if u.get("email") == email]
   
        if projeto and usuario:
            pid = projeto[0].get("id")
            uid = usuario[0].get("id")

            recurso = "projects/%s/members"%pid
            data = {"id":pid, "user_id":uid,"access_level":30}
            response = self._post(recurso,data)

            print  response.content
        else:
            print "Projeto ou usuario nao encontrado"


    def listar_projetos(self):
        recurso = "projects/all"
        response = self._get(recurso)
        projetos  = json.loads(response.content)
#        for p in projetos:
#            print p.get("name"), " - ", p.get("id")
#    
#        print len(projetos)
        return projetos

    def listar_usuarios(self):
        recurso = "users"
        response = self._get(recurso)
        usuarios  = json.loads(response.content)

#        for u in usuarios:
#            print u.get("name"), " - ", u.get("id"), " - ", u.get("email")
#    
#        print len(usuarios)
        return usuarios

if __name__ == '__main__':
    g = Gitlab()
    g.adicionar_desenvolvedor("Lord","alisson.menezes@responsus.com.br")
    #g.listar_usuarios()
    #g.adicionar_webhook("Lord","http://www.uol.com.br")
    #g.criar_usuario()
    #g.criar_projeto()
    #g.adicionar_webhook()
    #g.listar_projetos()
    
