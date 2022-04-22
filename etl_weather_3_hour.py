from datetime import date, datetime
import pandas as pd
import json



def run(file_name):
    with open(file_name,encoding='utf-8-sig') as json_file:
        data = json.load(json_file)

    schema ={
        #json attribute
        "Latitude.Value": float,
        "Longitude.Value": float,
        "Observe.WindDirection.Value": int,
        "Observe.Time": "datetime64",

        #lake attribute
        "report_dt": "datetime64",
        "dl_data_dt": "datetime64"
    }

    stations = data['Stations']
    df = pd.json_normalize(stations)
    df['report_dt'] = data['Header']['LastBuiltDate']
    df['dl_data_dt'] = datetime.now()

    for col, data_type in schema.items():
        if col == "Observe.WindDirection.Value":
            df[col] = df[col].str.replace(" ","").replace("",None)
        df[col] = df[col].astype(data_type)
    
    # change columns to lowercase
    df.columns= df.columns.str.strip().str.lower()
    df.columns = df.columns.str.replace(".", "_")
    
    file_name = f"{file_name.split('.')[0]}.parquet"
    df.to_parquet(file_name, index=None)
    return file_name

run("weather_3_hour/2022-03-10/11.json")