export FLASK_APP=./servidorWeb/servidor.py

all:
	sudo -E bash -c '. ./venv/bin/activate ;python3 -m flask run --host=0.0.0.0 -p 80'
	#python3 -m flask run 

venv-source:  
	. ./venv/bin/activate

escribe-paquetes:
	. ./venv/bin/activate
	pip freeze > requirements.txt
