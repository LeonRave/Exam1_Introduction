# introduction-quiz
Examen Leon Aguilar Jose Alejandro

#Synopsis

#Instalacion

**Instalar elastic**

Es el servidor que recibe la peticion post

wget http://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.0.2.tar.gz
tar -xzf elasticsearch-5.0.2.tar.gz
mv elasticsearch-5.0.2 elastic
cd elastic

**Iniciar elastic**

./bin/elasticsearch

**Crear y activar un entorno virtual**

virtualenv -p python 3.4 env
source env/bin/activate

**Instalar librerias**

pip install (librerias de requirments.txt)

**Librerias usadas**

import requests
import json

**Ejecutar el script send_answers.pya**

python send_answers.py

**Imprimir la respuesta del request**

curl -xGET 'http://localhost:9200/quiz/answer/1?pretty'

Para visualizarlo en elastic poner la misma url en el navegador.

**EL script**

El script recibe un json, lo lee y lo envia en una peticion post a elasticsearch
