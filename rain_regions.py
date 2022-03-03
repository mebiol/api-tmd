import requests
import json
from datetime import date
import os

with open('secret.json') as json_file:
    secrets = json.load(json_file)

uid = secrets['uid']
ukey = secrets['ukey']

url = f'https://data.tmd.go.th/api/RainRegions/v1/?uid={uid}&ukey={ukey}&format=json'

day = date.today()
y =  day.year
m =  day.month
x = requests.get(url)
decoded_data = x.text.encode().decode('utf-8-sig')
data = json.loads(decoded_data)

path = f"RainRegions/year={y}/month={m}"
os.makedirs(path, exist_ok=True)

with open(f'{path}/{day}.json', 'w',encoding = 'utf-8-sig') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)