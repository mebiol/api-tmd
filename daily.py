import requests
import json
from datetime import date
import os

list_api = [
    {
        "url" :"https://data.tmd.go.th/api/WeatherForecast7Days/V1/?type=json",
        "api_name" : "weather_forecast_7_day"
    },
    {
        "url": "https://data.tmd.go.th/api/WeatherToday/V1/?type=json",
        "api_name": "weather_today"
    }
]

for api in list_api:
    response = requests.request("GET", api['url']).json()
    day = date.today()
    y =  day.year
    m =  day.month

    path = f"{api['api_name']}/year={y}/month={m}"
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/{day}.json", 'w',encoding = 'utf-8-sig') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)