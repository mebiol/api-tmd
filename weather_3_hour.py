import requests
import json
from datetime import date,datetime
import os

url = "https://data.tmd.go.th/api/Weather3Hours/V1/?type=json"
response = requests.request("GET", url).json()
day = str(date.today())
dl = datetime.now()
print(dl.hour)

os.os.makedirs(f'weather_3_hour/{day}', exist_ok=True)

with open(f'weather_3_hour/{day}/{dl.hour}.json', 'w',encoding = 'utf-8-sig') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)
print(type(response))