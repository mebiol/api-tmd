import requests
import json
from datetime import date,datetime
import os

url = "https://data.tmd.go.th/api/WeatherForecastDaily/V1/?type=json"
response = requests.request("GET", url).json()
day = str(date.today())
dl = datetime.now()

if os.path.exists(day) == False:
    os.makedirs(f'weather_forecast_daily/{day}', exist_ok=True)

with open(f'weather_forecast_daily/{day}/{day}.json', 'w',encoding = 'utf-8-sig') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)
print(type(response))