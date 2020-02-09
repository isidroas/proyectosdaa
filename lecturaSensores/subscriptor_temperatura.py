#import context  # Ensures paho is in PYTHONPATH
import paho
import paho.mqtt.client as mqtt
import time
import sensoresMet

def on_connect(mqttc, obj, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        global Connected
        Connected = True
    else:
        print("Ha fallado la conexion")

##############################################################################
####################### MENSAJE RECIBIDO EN EL TOPIC #########################
# Esta es la funcion que se encarga de recoger el mensaje del topic que sea 
# (mas abajo se define) y lo manda a donde sea necesario. En este caso a una web
def on_message(mqttc, obj, msg):
    tiempo = time.time();
    print(msg.topic + " " + str(msg.payload))
    #with open('/home/pi/paho_mqtt_repo/test.txt','a+') as f:
        #f.write("Mensaje recibido: " + msg.payload + " " + str(tiempo) + "\n")
    temperatura =  float(msg.payload)
    #print(temperatura)
    sensoresMet.enviaSensor(temperatura,"sensorTemp")
    
        
###############################################################################
Connected = False

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("temperatura", 0)

mqttc.loop_forever()
