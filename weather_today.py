import requests
import json
from datetime import date,datetime
import os
import time

url = "https://data.tmd.go.th/api/WeatherToday/V1/?type=json"
response = requests.request("GET", url).json()
day = str(date.today())
y = date.today.strftime("%Y")
m = date.today.strftime("%m")

path = f'weather_today/year={y}/month={m}'
os.makedirs(path, exist_ok=True)

with open(f'{path}/{day}.json', 'w',encoding = 'utf-8-sig') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)
print(type(response))

