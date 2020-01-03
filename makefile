export FLASK_APP=./servidorWeb/servidor.py


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

.PHONY: baseDatosServ
baseDatosServ: 
	(\
		. ./venv/bin/activate; \
		python3 baseDatosServ/baseDatosServ.py; \
	)


all: 
	(\
		. ./venv/bin/activate; \
		python3 baseDatosServ/baseDatosServ.py; \
	)&
	(\
		. ./venv/bin/activate; \
		python3 ./sensoresMeteo.py; \
	)&
	sudo -E bash -c '. ./venv/bin/activate ;python3 -m flask run --host=0.0.0.0 -p 80'

