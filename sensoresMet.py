import time
from random import random
from manejaMiddleware import enviaDatos 

def enviaSensor(dato,tipo):
    tiempo=time.time()
    paqueteEnviar={}
    # Mirar el archivo parametros.yaml para ver que claves se le pueden añadir al diccionario
    paqueteEnviar[tipo]={'valor':dato,'tiempo': tiempo}
    print(paqueteEnviar)
    enviaDatos(paqueteEnviar)


