import flask
from flask import render_template, jsonify

import time
import sys
sys.path.append('../')
from manejaBaseDatos import recibeDatos 

app = flask.Flask(__name__)

@app.route('/')
def principal():
    paqueteEnviar=['sensorTemp']
    datos=recibeDatos(paqueteEnviar)
    return render_template('index.html',temp=datos['sensorTemp']['valor'])

