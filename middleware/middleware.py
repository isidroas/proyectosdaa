from multiprocessing.connection import Listener
import yaml

# Diccionario con los últimos datos de los sensores
sensores={}

# Lista con el nombre de cada uno de los sensores
listaSensores=[]

puerto=5000

def cargarParametros():
    with open(r'./parametros.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        parametros = yaml.load(file, Loader=yaml.FullLoader)
        global listaSensores
        listaSensores=parametros['sensores']
        global puerto
        puerto = parametros['puerto']

cargarParametros()
# Valor inicial a los datos 
for i in listaSensores:
    sensores[i]={'valor':1.0, 'tiempo':0} # Valor cualquiera para inicializar


list=Listener(address=('localhost',puerto))
while True:
    con=list.accept()
    datos=con.recv()

    if type(datos)==type({}):
        # Es un diccionario. Solo hay que devolver ACK
        print( 'datos es un diccionario')
        sensores.update(datos)
        print(sensores)
        con.send("ACK")
    elif type(datos)==type([]):
        # Es un lista. Hay que devolver un diccionario 
        print( 'datos es una lista')
        print(datos)
        paqueteEnviar={}
        for i in datos:
            paqueteEnviar[i]=sensores[i]
        con.send(paqueteEnviar)
    else:
        print( 'no es ni diccionario ni lista')

    con.close()
list.close()

