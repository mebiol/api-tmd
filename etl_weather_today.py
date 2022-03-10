from datetime import date, datetime
from numpy import datetime64
import pandas as pd
import json


file_name = 'weather_today/year=2022/month=3/2022-03-02.json'
with open(file_name,encoding='utf-8-sig') as json_file:
    json_file = json.load(json_file)


weather_today_schema ={
    "Latitude.Value": float,
    "Longitude.Value": float,
    "Observe.Time": datetime64,
    "Observe.WindDirection.Value": int
}

stations = json_file['Stations']
df = pd.json_normalize(stations)
df = df.dropna(how='all')

for col, data_type in weather_today_schema.items():
    df[col] = df[col].str.replace(" ","").replace("",None)
    df[col] = df[col].astype(data_type)
    
# change columns to lowercase
df.columns= df.columns.str.strip().str.lower()
# replace columns_name "." > "_"
df.columns = df.columns.str.replace(r"[.]", "_")
print(df.columns)
# save to csv
df.to_csv('Weather_today.csv',index=None,encoding='utf-8-sig')