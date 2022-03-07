from unittest import result
import pandas as pd
import json


with open('RainRegions/year=2022/month=3/2022-03-03.json',encoding = 'utf-8-sig') as json_file:
    data = json.load(json_file)['Regions']



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


for r in data['Region']:
    if type(r['Provinces']['Province']) == dict:
        p = r['Provinces']['Province']
        extract_data(r['RegionName'], p)

    else:
        for p in r['Provinces']['Province']:
            extract_data(r['RegionName'], p)

df = pd.DataFrame(results)
df.to_csv('etl_rain_regions.csv',index=None,encoding='utf-8-sig')