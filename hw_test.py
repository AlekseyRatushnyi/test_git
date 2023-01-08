import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)