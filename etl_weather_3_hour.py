from datetime import date, datetime
from numpy import datetime64
import pandas as pd
import json


file_name = 'weather_3_hour/2022-03-02/13.json'
with open(file_name,encoding='utf-8-sig') as json_file:
    json_file = json.load(json_file)


schema ={
    "Latitude.Value": float,
    "Longitude.Value": float,
    "Observe.WindDirection.Value": int,
    "Observe.Time": datetime64
}

stations = json_file['Stations']
df = pd.json_normalize(stations)
df = df.dropna(how='all')

for col, data_type in schema.items():
    if col == "Observe.WindDirection.Value":
        df[col] = df[col].str.replace(" ","").replace("",None)
    df[col] = df[col].astype(data_type)
    
# change columns to lowercase
df.columns= df.columns.str.strip().str.lower()
# replace columns_name "." > "_"
df.columns = df.columns.str.replace(r"[.]", "_")
print(df.columns)
# save to csv
df.to_csv('Weather_3_hour.csv',index=None,encoding='utf-8-sig')