import time
from random import random
from manejaBaseDatos import enviaDatos 


while True:
    Lum=random()*2+35
    Temp=random()*1+20
    tiempo=time.time()
    paqueteEnviar={}
    paqueteEnviar['sensorLum']={'valor':Lum,'tiempo': tiempo} # Mirar el archivo parametros.yaml para ver que claves se le pueden añadir al diccionario
    paqueteEnviar['sensorTemp']={'valor':Temp,'tiempo': tiempo}
    print(paqueteEnviar)
    enviaDatos(paqueteEnviar)

    time.sleep(1)

