#!/usr/bin/python


import jenkins
from lxml import etree

class Jenkins:
    def __init__(self):
        self.server = jenkins.Jenkins("http://192.168.0.4:8080")
        print self.server.get_version()

    def criar_job(self,nome):
       # xml = self._criar_job_steps()  
       
        with open("template.xml","r") as f:
            xml = f.read()
        root = etree.XML(xml)
        
        for b in root.findall("builders"):
            builder = b
        
        with open("deploy.txt","r") as d:
            for l in d.readlines():
                elemento_shell = etree.Element("hudson.tasks.Shell")
                elemento_command = etree.Element("command")             
                elemento_command.text = l
                elemento_shell.append(elemento_command)
                builder.append(elemento_shell)
                
        root = etree.tostring(root)
        self.server.create_job(nome,root)                
       # print root
        return root            


    def _criar_job_steps(self):
        with open("template.xml","r") as f:
            xml = f.read()
        root = etree.XML(xml)
        with open("deploy.txt","r") as d:
            txt = d.read()
       
        for b in root.findall("builders"):
            builder = b

#        for c in builder.iterchildren():
#            #print c.tag
#            for sc in c.iterchildren():
#                #print sc.tag, sc.text
                
        elemento_shell = etree.Element("hudson.tasks.Shell")
        elemento_command = etree.Element("command")
        elemento_command.text = "apt-get update"
        elemento_command.text = txt
        elemento_shell.append(elemento_command)
        builder.append(elemento_shell)
        root = etree.tostring(root)

     
        

#**kwargs parametros nao obrigatorios         
    def executar_job(self,nome,**kwargs):  
        self.server.build_job(nome,kwargs)


if __name__ == '__main__':
    j = Jenkins()
   # j.executar_job("JobTesteTxt",APPNAME="container_teste",PORTA=81)
    j.criar_job("teste")



