#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('baseDatos/datosMeteo.db')
c = conn.cursor()
c.execute('''CREATE TABLE sensorTemp  
                     (valor float, tiempo int)''')
c.execute(' INSERT INTO sensorTemp VALUES (1.0,0)')
conn.commit()
conn.close()

