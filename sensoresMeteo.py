import time
from random import random
import sys
from manejaMiddleware import enviaDatos 


while True:
    Hum=random()*2+35
    Temp=random()*1+20
    Pres=random()*1+25
    tiempo=time.time()
    paqueteEnviar={}
    # Mirar el archivo parametros.yaml para ver que claves se le pueden añadir al diccionario
    paqueteEnviar['sensorHum']={'valor':Hum,'tiempo': tiempo}
    paqueteEnviar['sensorTemp']={'valor':Temp,'tiempo': tiempo}
    paqueteEnviar['sensorPres']={'valor':Pres,'tiempo': tiempo}
    print(paqueteEnviar)
    enviaDatos(paqueteEnviar)

    time.sleep(1)

