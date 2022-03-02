import requests
import json
from datetime import date
import os


url = "https://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json"
response = requests.request("GET", url).json()
day = date.today()
y =  day.year
m =  day.month

path = f'weather_forecast_7_day/year={y}/month={m}'
os.makedirs(path, exist_ok=True)

with open(f'{path}/{day}.json', 'w',encoding = 'utf-8-sig') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)
print(type(response))