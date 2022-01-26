import json
from shutil import copyfile 

#ruta = "/home/nian/Documentos/composerAutomation/composer.json"
#archivo = open(ruta, 'r')

with open("composer.json") as myJson:
    datos = json.loads(myJson.read())

#print(datos["require"]['bits/oneapp_adminimal'])


def modificarDatos(datos):
    for d in datos["require"],:
        #print(f"{d}\n")
        x = d['bits/express_auth']
        print(x)
        if x != '1.0.8':
            d.update({'bits/express_auth':'1.0.8'})
        else:
            print("es igual")
            
        print(d['bits/express_auth'])
        myJson.close()
        

    


# for d in datos["require"],:
#     #print(f"{d}\n")
#     x = d['bits/express_auth']
#     print(x)
#     if x != '1.0.7':
#         d.update({'bits/express_auth':'1.0.7'})
#     else:
#         print("es igual")



# print(d['bits/express_auth'])
# myJson.close()   
    
print("\n===========================================================\n")

# print(datos)

print("\n===========================================================\n")


def generarJson(datos):
    s = json.dumps(datos,indent=4) #convertirlo a texto oara guardar como json
    print(s)
    f = open("composer.json","w")
    f.write(s)
    f.close()
    

# s = json.dumps(datos,indent=4) #convertirlo a texto oara guardar como json
# #print(s)
# f = open("composer.json","w")
# f.write(s)
# f.close()

modificarDatos(datos)
generarJson(datos)

print("\n===========================================================\n")
copyfile("/home/nian/Documentos/composerAutomation/composer.json", "/home/nian/Documentos/composerAutomation/escritura2.txt")


