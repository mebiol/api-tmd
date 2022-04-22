import requests
import json
from datetime import date,datetime
import os
import time

with open('secrets.json') as json_file:
    secrets = json.load(json_file)

uid = secrets['uid']
ukey = secrets['ukey']

list_api = [
    {
        "url" :"https://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json",
        "api_name" : "weather_forecast_7_day"
    },
    {
        "url": "https://data.tmd.go.th/api/WeatherToday/V1/?type=json",
        "api_name": "weather_today"
    },
    {
        "url": f"https://data.tmd.go.th/api/RainRegions/v1/?uid={uid}&ukey={ukey}&format=json",
        "api_name": "rain_region"
    }
]

for api in list_api:
    response = requests.request("GET", api['url'])
    day = date.today()
    y =  day.year
    m =  day.month
    decoded_data = response.text.encode().decode('utf-8-sig')
    data = json.loads(decoded_data)

    path = f"{api['api_name']}/year={y}/month={m}"
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/{day}.json", 'w',encoding = 'utf-8-sig') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        