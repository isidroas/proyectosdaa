#!/usr/bin/python

import sqlite3
import time

from manejaMiddleware import recibeDatos

def ultimoTiempo(): 
    conn = sqlite3.connect('baseDatos/datosMeteo.db')
    c = conn.cursor()
    c.execute(''' SELECT tiempo FROM  sensorTemp ORDER BY tiempo DESC ''')
    ultimaMedida=c.fetchone()[0]
    conn.close()
    return ultimaMedida

def incluyeMedida(biblio):
    conn = sqlite3.connect('baseDatos/datosMeteo.db')
    c = conn.cursor()
    medida=biblio['sensorTemp']
    c.execute(' INSERT INTO sensorTemp VALUES (?,?)',[medida['valor'],medida['tiempo']])
    medida=biblio['sensorHum']
    c.execute(' INSERT INTO sensorHum VALUES (?,?)',[medida['valor'],medida['tiempo']])
    medida=biblio['sensorPres']
    c.execute(' INSERT INTO sensorPres VALUES (?,?)',[medida['valor'],medida['tiempo']])
    conn.commit()
    conn.close()

#def creaLista(): 
#    conn = sqlite3.connect('baseDatos/datosMeteo.db')
#    c = conn.cursor()
#    c.execute(''' SELECT * FROM  sensorTemp ORDER BY tiempo DESC ''')
#    lista=c.fetchmany(24)
#    lista2=[]
#    for x in lista:
#        lista2.append({'valor': x[0], 'hora': time.gmtime(x[1]).tm_hour})
#    conn.close()
#    return lista2 


while True:
    nuevaMedida=recibeDatos(['sensorTemp', 'sensorHum', 'sensorPres'])

    print(" BASE DE DATOS --- LA NUEVA MEDIDA ES: ") 
    print(nuevaMedida)
    tiempoNuevaMedida=nuevaMedida['sensorTemp']['tiempo']
    horaNuevaMedida=time.gmtime(tiempoNuevaMedida).tm_hour
    tiempoUltimaMedida=ultimoTiempo()
    horaUltimaMedida=time.gmtime(tiempoUltimaMedida).tm_hour
    print("--- LA NUEVA Y ULTIMA MEDIDA SON ---")
    print(horaNuevaMedida)
    print(horaUltimaMedida)
    print(tiempoNuevaMedida)
    print(tiempoUltimaMedida)

    #if( (tiempoNuevaMedida - tiempoUltimaMedida)>0 and (horaNuevaMedida-horaUltimaMedida)!=0 ):
    if( (tiempoNuevaMedida - tiempoUltimaMedida)>3600  ):
        print(' -------- BASE DE DATOS ----- NUEVA MEDIDA ---')
        incluyeMedida(nuevaMedida)
        #lista=creaLista()
        #paquete={'sensorTempHist': lista}
        print(nuevaMedida)
        #enviaDatos(paquete)
    time.sleep(3600)
