import flask
from flask import render_template, jsonify, send_from_directory

import time
import sys
sys.path.append('../')
from manejaMiddleware import recibeDatos 

app = flask.Flask(__name__)

#@app.route('/')
#def principal():
#    paqueteEnviar=['sensorTemp']
#    datos=recibeDatos(paqueteEnviar)
#    return render_template('index.html',temp=datos['sensorTemp']['valor'])

#@app.route('/dynamicChart')
#def dynamicChart():
#    return render_template('dynamicChart.html')

@app.route('/')
def chartjs():
    return render_template('chartjs.html')

@app.route('/devuelveDatos',methods=['POST'])
def devuelveDatos():
    #print(" Se ha recibido un Ajax:")
    datos1=flask.request.form
    #print(datos1)
    peticiones=datos1.getlist("datos[]")
    
    #print(peticiones)
    datos=recibeDatos(peticiones)
    #print("Se va a enviar por ajax al cliente:")
    #print(datos)
    return jsonify(datos )

@app.route('/descarga', methods=['GET', 'POST'])
def download():
    return send_from_directory(directory='/home/pi/proyectoSDAA/baseDatos', filename='datosMeteo.db')



@app.route('/js/<path:path>', methods=['GET', 'POST'])
def js_files(path):
    return send_from_directory(directory='/home/pi/proyectoSDAA/servidorWeb/sqlite-viewer/js', filename=path)

@app.route('/css/<path:path>', methods=['GET', 'POST'])
def cs_files(path):
    return send_from_directory(directory='/home/pi/proyectoSDAA/servidorWeb/sqlite-viewer/css', filename=path)

@app.route('/img/<path:path>', methods=['GET', 'POST'])
def img_files(path):
    return send_from_directory(directory='/home/pi/proyectoSDAA/servidorWeb/sqlite-viewer/img', filename=path)

@app.route('/fonts/<path:path>', methods=['GET', 'POST'])
def fonts_files(path):
    return send_from_directory(directory='/home/pi/proyectoSDAA/servidorWeb/sqlite-viewer/fonts', filename=path)

@app.route('/sql-viewer', methods=['GET', 'POST'])
def database():
    return send_from_directory(directory='/home/pi/proyectoSDAA/servidorWeb/sqlite-viewer/', filename='index.html')
