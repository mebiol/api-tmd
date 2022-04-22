import pandas as pd
from datetime import datetime
import json


def run(file_name):
    with open(file_name, encoding = 'utf-8-sig') as json_file:
        data = json.load(json_file)
    datas = data['Regions']

    schema ={
        #json attribute
        "Latitude": float,
        "Longitude": float,
        "Rainfall": float,

        #lake attribute
        "report_dt": "datetime64",
        "dl_data_dt": "datetime64"
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
    df['dl_data_dt'] = datetime.now()
    for col, data_type in schema.items():
        try:
            df[col] = df[col].astype(data_type)
        except:
            print(f"fix column {col}")
            fix = []
            for data in df[col]:
                try:
                    fix.append(float(data))
                except:
                    fix.append(None)
            df[col] = fix

    # change columns to lowercase
    df.columns= df.columns.str.strip().str.lower()
    df.columns = df.columns.str.replace(r"[.]", "_")
    
    file_name = f"{file_name.split('.')[0]}.parquet"
    df.to_parquet(file_name, index=None)
    return file_name

run("rain_regions/year=2022/month=3/2022-03-07.json")