import requests

url = 'https://shop.hasbro.com/worldwide'
response = requests.get(url)

print(response.headers,'\n ------------headers------------ \n') #заголовки http ответа
print(response.status_code, '\n ------------status_code------------\n') #код статуса
print(response.request, '\n ------------request------------ \n') #тип запроса
print(response.content, '\n ------------content------------ \n') #возврат значения ответа в байтах



