import multiprocessing.connection
import sys
import yaml

# Variable global que guarda el número de puerto. Aquí se establece el valor por defecto, pero más tarde se actualizará mediante un archivo de parámetros
puerto=5000

#with open(r'/home/pi/proyectoSDAA/parametros.yaml') as file:
with open(r'./parametros.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    parametros = yaml.load(file, Loader=yaml.FullLoader)
    #print(type(parametros['sensores'].items()))
    puerto=parametros['puerto']


def enviaDatos(paquete):
    con = multiprocessing.connection.Client(address=('localhost',puerto))
    con.send(paquete)
    resp=con.recv()
    if resp!='ACK':
        print('La base de datos no ha respondido con ACK')

def recibeDatos(paquete):
    con = multiprocessing.connection.Client(address=('localhost',puerto))
    con.send(paquete)
    resp=con.recv()
    return resp

