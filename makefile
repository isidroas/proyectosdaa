export FLASK_APP=./servidorWeb/servidor.py
export PYTHONPATH=$PYTHONPATH:/home/pi/proyectoSDAA


.PHONY: venv-source
venv-source:  
	. ./venv/bin/activate

escribe-paquetes:
	. ./venv/bin/activate
	pip freeze > requirements.txt

.PHONY: elimina-procesos
elimina-procesos:  
	sudo pkill python && (\
		echo "Se han terminado los procesos python"\
		) || (\
		echo " No habia procesos python"\
		)
	sudo systemctl start mosquitto.service
	#sudo pkill mosquitto && (\
	#	echo "Se han terminado los procesos mosquito"\
	#	) || (\
	#	echo " No habia procesos mosquito"\
	#	)

.PHONY: servidorWeb
servidorWeb:
	sudo -E bash -c '. ./venv/bin/activate ;python3 -m flask run --host=0.0.0.0 -p 80'

.PHONY: sensoresMeteo
sensoresMeteo: 
	(\
		. ./venv/bin/activate; \
		python3 ./lecturaSensores/subscriptor_temperatura.py; \
	)

.PHONY: middleware
middleware: 
	(\
		. ./venv/bin/activate; \
		python3 middleware/middleware.py; \
	)

.PHONY: baseDatos
baseDatos: 
	(\
		. ./venv/bin/activate; \
		python3 baseDatos/baseDatos.py; \
	)

.PHONY: crearBaseDatos
crearBaseDatos: 
	(\
		. ./venv/bin/activate; \
		python3 baseDatos/creaBaseDatos.py; \
	)

.PHONY: eliminaBaseDatos
eliminaBaseDatos: 
	rm baseDatos/datosMeteo.db


all: elimina-procesos
	rm *.log || (echo "no habia ficheros log")
	#mosquitto -c mosquitto.conf -d
	#mosquitto > mosquitto.log &
	(\
		. ./venv/bin/activate; \
		python3 middleware/middleware.py; \
	)&
	sleep 1
	(\
		. ./venv/bin/activate; \
		python3 ./lecturaSensores/subscriptor_temperatura.py; \
	)&
	(\
		. ./venv/bin/activate; \
		python3 ./lecturaSensores/subscriptor_humedad.py; \
	)&
	(\
		. ./venv/bin/activate; \
		python3 ./lecturaSensores/subscriptor_presion.py; \
	)&
	(\
		. ./venv/bin/activate; \
		python3 baseDatos/baseDatos.py; \
	)&
	sudo -E bash -c '. ./venv/bin/activate ;python3 -m flask run --host=0.0.0.0 -p 80'

