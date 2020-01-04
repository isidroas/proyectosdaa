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
	sudo pkill python


.PHONY: servidorWeb
servidorWeb:
	sudo -E bash -c '. ./venv/bin/activate ;python3 -m flask run --host=0.0.0.0 -p 80'

.PHONY: sensoresMeteo
sensoresMeteo: 
	(\
		. ./venv/bin/activate; \
		python3 ./sensoresMeteo.py; \
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


all: 
	(\
		. ./venv/bin/activate; \
		python3 middleware/middleware.py; \
	)&
	(\
		. ./venv/bin/activate; \
		python3 ./sensoresMeteo.py; \
	)&
	sudo -E bash -c '. ./venv/bin/activate ;python3 -m flask run --host=0.0.0.0 -p 80'

