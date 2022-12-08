import json
import pandas as pd
import requests

city = input("Enter City Name ")
date = input("Enter Date yyyy-mm-dd ")
URL = 'https://api.oikolab.com/weather'
API_KEY = '658443fc024c4031a1b676c5accdcb17'
resp = requests.get(URL,
                 params={'param': ['temperature',],

                         'start': date,
                         'location' : city,
                         'end': date,
                         'freq': 'D',
                         'api-key': API_KEY}
                 )
weather_data = json.loads(resp.json()['data'])
df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],
                                       unit='s'),
                  data=weather_data['data'],
                  columns=weather_data['columns'])

#print(weather_data)
temp = int(df.iloc[0,4])
print(f"Temperature for {city} on {date} = {temp}C")
