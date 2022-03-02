import requests
import json
from datetime import date
import os
import codecs

url = 'https://data.tmd.go.th/api/RainRegions/v1/?uid=api&ukey=api12345&format=json'
secret = {'u65thunchanok1944': ' 65f231a480a39c7e52027023980c35b8'}
day = date.today()
y =  day.year
m =  day.month

x = requests.get(url, data = secret)
print(x)
decoded_data = x.text.encode().decode('utf-8-sig')
data = json.loads(decoded_data)
print(type(data))

path = f'RainRegions/year={y}/month={m}'
os.makedirs(path, exist_ok=True)

with open(f'{path}{day}.json', 'w',encoding = 'utf-8-sig') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)