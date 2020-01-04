#!/usr/bin/python

import sqlite3
import time

from manejaMiddleware import recibeDatos, enviaDatos

def ultimoTiempo(): 
    conn = sqlite3.connect('baseDatos/datosMeteo.db')
    c = conn.cursor()
    c.execute(''' SELECT tiempo FROM  sensorTemp ORDER BY tiempo DESC ''')
    ultimaMedida=c.fetchone()[0]
    conn.close()
    return ultimaMedida

def incluyeMedida(medida):
    conn = sqlite3.connect('baseDatos/datosMeteo.db')
    c = conn.cursor()
    c.execute(' INSERT INTO sensorTemp VALUES (?,?)',[medida['valor'],medida['tiempo']])
    conn.commit()
    conn.close()

def creaLista(): 
    conn = sqlite3.connect('baseDatos/datosMeteo.db')
    c = conn.cursor()
    c.execute(''' SELECT * FROM  sensorTemp ORDER BY tiempo DESC ''')
    lista=c.fetchmany(24)
    lista2=[]
    for x in lista:
        lista2.append({'valor': x[0], 'hora': time.gmtime(x[1]).tm_hour})
    conn.close()
    return lista2 


while True:
    nuevaMedida=recibeDatos(['sensorTemp'])

    print(nuevaMedida)
    tiempoNuevaMedida=nuevaMedida['sensorTemp']['tiempo']
    horaNuevaMedida=time.gmtime(tiempoNuevaMedida).tm_hour
    tiempoUltimaMedida=ultimoTiempo()
    horaUltimaMedida=time.gmtime(tiempoUltimaMedida).tm_hour

    if( (tiempoNuevaMedida - tiempoUltimaMedida)>0 and (horaNuevaMedida-horaUltimaMedida)!=0 ):
        print(' se va a incluir una medida')
        incluyeMedida(nuevaMedida['sensorTemp'])
        lista=creaLista()
        paquete={'sensorTempHist': lista}
        print(paquete)
        enviaDatos(paquete)
    time.sleep(3600)
