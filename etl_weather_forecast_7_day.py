from datetime import date, datetime
from numpy import datetime64
import pandas as pd
import json


def run(file_name):
    with open(file_name,encoding='utf-8-sig') as json_file:
        data = json.load(json_file)
    provinces = data['Provinces']

    schema ={
        #json attribute
        "MaxTemperature.Value": int,
        "MinTemperature.Value": int,
        "WindDirection.Value": int,
        "WindSpeed.Value": int,
        "Rain.Value": int,
        "Date": "datetime64",

        #lake attribute
        "report_dt": "datetime64",
        "dl_data_dt": "datetime64"
    }

    df = pd.DataFrame()
    for prov in provinces:
        df_prov = pd.json_normalize(prov['SevenDaysForecast'])
        df_prov['ProvinceNameTh'] = prov['ProvinceNameTh']
        df_prov['ProvinceNameEng'] = prov['ProvinceNameEng']
        df = pd.concat([df,df_prov])

    df['report_dt'] = data['Header']['LastBuiltDate']
    df['dl_data_dt'] = datetime.now()
    for col, data_type in schema.items():
        df[col] = df[col].astype(data_type)

    # change columns to lowercase
    df.columns= df.columns.str.strip().str.lower()
    df.columns = df.columns.str.replace(".", "_")
    
    file_name = f"{file_name.split('.')[0]}.parquet"
    df.to_parquet(file_name, index=None)
    return file_name

run(file_name ='weather_forecast_7_day/year=2022/month=3/2022-03-10.json')