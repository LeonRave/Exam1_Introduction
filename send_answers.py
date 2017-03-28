import json
import requests
datos = json.loads(open('introduction_quiz.json').read())

for fila in datos['quiz']:
	print(fila['question'])
	print(fila['answer']

response=requests.post("http://localhost:9200/quiz/answer/5", json=datos)
print(response)







