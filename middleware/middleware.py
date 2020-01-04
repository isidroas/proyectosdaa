from multiprocessing.connection import Listener
import yaml

# Diccionario con los últimos datos de los sensores
sensores={}

def cargarParametros():
    with open(r'/home/pi/proyectoSDAA/parametros.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        parametros = yaml.load(file, Loader=yaml.FullLoader)
        listaSensores=parametros['sensores']
        for i in listaSensores:
            sensores[i]={'valor':1.0, 'tiempo':0} # Valor cualquiera para inicializar
        print(sensores)

cargarParametros()

list=Listener(address=('localhost',6000))
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

