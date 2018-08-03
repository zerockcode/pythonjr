#https://westus.api.cognitive.microsoft.com/emotion/v1.0
#
#ba3abae58fee5489bafc741e93f935610
#ba79e21b5330644959d92704f46b989e3

import requests


headers = {}
headers['Ocp-Apim-Subscription-Key'] = 'ba79e21b5330644959d92704f46b989e3'
headers['Content-Type'] = 'application/json'


urlImage = 'http://cfile9.uf.tistory.com/image/2426123D562AE6252A33B9'
json = { 'url': urlImage }
data = None
params = None

_url ="https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"


bytes = open('C:\\zzz\\test.jpg', 'rb').read()
data = bytes

try:
    response  = requests.request('post', _url, json=json, data=data, headers=headers, params=params)
    result = response.content

    print(result)

except Exception as e:
    print("error ")
    print(e)