import json
from shutil import copyfile 

#ruta = "/home/nian/Documentos/composerAutomation/composer.json"
#archivo = open(ruta, 'r')

with open("composer.json") as myJson:
    datos = json.loads(myJson.read())

with open("composer2.json") as myJson2:
    datos2 = json.loads(myJson2.read())


datos.update(datos2)
myJson.close()
myJson2.close()

#print(datos)

def generarJson(datos):
    s = json.dumps(datos,indent=4) #convertirlo a texto oara guardar como json
    print(s)    
    f = open("composer.json","w")
    f.write(s)
    f.close()

generarJson(datos)

