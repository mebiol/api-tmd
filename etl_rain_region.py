from unittest import result
from numpy import datetime64
import pandas as pd
import json


with open('RainRegions/year=2022/month=3/2022-03-03.json',encoding = 'utf-8-sig') as json_file:
    data = json.load(json_file)
datas = data['Regions']

schema ={
    "Latitude": float,
    "Longitude": float
}


results = []
def extract_data(RegionName:str, p:dict):
    result = {}
    if type(p['Stations']['Station']) == dict:
        result = p['Stations']['Station'].copy()
        result['RegionName'] = RegionName
        result['ProvinceName'] = p['ProvinceName']
        results.append(result)
    else:
        for s in p['Stations']['Station']:
            result = s.copy()
            result['RegionName'] = RegionName
            result['ProvinceName'] = p['ProvinceName']
            results.append(result)


for r in datas['Region']:
    if type(r['Provinces']['Province']) == dict:
        p = r['Provinces']['Province']
        extract_data(r['RegionName'], p)

    else:
        for p in r['Provinces']['Province']:
            extract_data(r['RegionName'], p)

df = pd.DataFrame(results)
df['report_dt'] = data['Header']['DateOfData']

for col, data_type in schema.items():
    df[col] = df[col].str.replace(" ","").replace("",None)
    df[col] = df[col].astype(data_type)


# change columns to lowercase
df.columns= df.columns.str.strip().str.lower()
# save to csv
df.to_csv('rain_region.csv',index=None,encoding='utf-8-sig')