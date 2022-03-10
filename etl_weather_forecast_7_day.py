from datetime import date, datetime
from numpy import datetime64
import pandas as pd
import json


file_name = 'weather_forecast_7_day/year=2022/month=3/2022-03-02.json'
with open(file_name,encoding='utf-8-sig') as json_file:
    json_file = json.load(json_file)
data = json_file['Provinces']

schema ={
    "max_temperature": int,
    "min_temperature": int,
    "wind_direction": int,
    "wind_speed": int,
    "rain":int,
    "date":datetime64   
}

list_name_th =[]
list_name_en =[]
list_date=[]
list_maxtem=[]
list_maxtem_unit=[]
list_mintem=[]
list_mintem_unit=[]
list_winddirection=[]
list_winddirection_unit=[]
list_windspeed=[]
list_windspeed_unit=[]
list_rain=[]
list_rain_unit=[]
list_descript_th=[]
list_descript_en=[]
list_wave_hight_th=[]
list_wave_hight_en=[]
list_tem_level=[]
list_tem_level_en=[]


for i in data:
    for j in i['SevenDaysForecast']:
        dates = j['Date']
        list_date.append(dates)
        maxtemp = j['MaxTemperature']['Value']  
        list_maxtem.append(maxtemp)
        maxtemp_unit = j['MaxTemperature']['Unit']
        list_maxtem_unit.append(maxtemp_unit)
        mintemp = j['MinTemperature']['Value']
        list_mintem.append(mintemp)
        mintemp_unit = j['MinTemperature']['Unit']
        list_mintem_unit.append(mintemp_unit)
        win_direct = j['WindDirection']['Value']
        list_winddirection.append(win_direct)
        win_direct_unit = j['WindDirection']['Unit']
        list_winddirection_unit.append(win_direct_unit)
        win_speed = j['WindSpeed']['Value']
        list_windspeed.append(win_speed)
        win_speed_unit = j['WindSpeed']['Unit']
        list_windspeed_unit.append(win_speed_unit)
        rain = j['Rain']['Value']
        list_rain.append(rain)
        rain_unit = j['Rain']['Unit']
        list_rain_unit.append(rain_unit)
        descript_th = j['WeatherDescription']
        list_descript_th.append(descript_th)
        descript_en = j['WeatherDescriptionEn']
        list_descript_en.append(descript_en)
        wave_height = j['WaveHeight']
        list_wave_hight_th.append(wave_height)
        wave_height_en = j['WaveHeightEn']
        list_wave_hight_en.append(wave_height_en)
        tem_level = j['TempartureLevel']
        list_tem_level.append(tem_level)
        tem_level_en = j['TempartureLevelEn']
        list_tem_level_en.append(tem_level_en)
        if "celcius" in list_maxtem_unit:
            a = i['ProvinceNameTh']
            b = i['ProvinceNameEng']
            list_name_th.append(a)
            list_name_en.append(b)
        else:
            print('error')


result = {'date': list_date, 'provincenameth': list_name_th, 'provincenameeng': list_name_en,
          'max_temperature' : list_maxtem,'max_temperature_unit' : list_maxtem_unit,
          'min_temperature' : list_mintem, 'min_temperature_unit' : list_mintem_unit,
          'wind_direction' : list_winddirection, 'wind_direction_unit' : list_winddirection_unit,
          'wind_speed' : list_windspeed , 'wind_speed_unit' : list_windspeed_unit,
          'rain': list_rain, 'rain_unit' : list_rain_unit, 'descirtion_th' : list_descript_th,
          'descirtion_en' : list_descript_en, 'waveheight' : list_wave_hight_th,
          'waveheight_en' : list_wave_hight_en,'temparturelevel' : list_tem_level,
          'temparturelevelEng' : list_tem_level_en } 

df = pd.DataFrame.from_dict(result, orient='index')
df = df.transpose()

for col, data_type in schema.items():
    # df[col] = df[col].str.replace(" ","").replace("",None)
    df[col] = df[col].astype(data_type)
# save to csv
df.to_csv('weather_forecast_7_day.csv',index=None,encoding='utf-8-sig')