import json
import pandas as pd
import requests
import datetime

# city = input("Enter City Name ")
# date = input("Enter Date yyyy-mm-dd ")

def get_temp_var(city, start_date, end_date):
    
    URL = 'https://api.oikolab.com/weather'
    API_KEY = '658443fc024c4031a1b676c5accdcb17'
    resp = requests.get(URL,
                    params={'param': ['temperature',],

                            'start': start_date,
                            'location' : city,
                            'end': end_date,
                            'freq': 'D',
                            'api-key': API_KEY}
                    )
    #print(resp.json())
    weather_data = json.loads(resp.json()['data'])
    df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],
                                        unit='s'),
                    data=weather_data['data'],
                    columns=weather_data['columns'])

    # print(weather_data)
    # temp = df.iloc[0,4]
    # print(f"Tempertature for {city} on {date} = {temp}C")
    variance = df['temperature (degC)'].var()
    # print(variance)
    return variance

city1 = input()
city2 = input()
start_date = input()
start_date = start_date.split('-')
obj1 = datetime.datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))
obj2 = obj1 + datetime.timedelta(days =7)

start_date = obj1.strftime('%y-%m-%d')
end_date = obj2.strftime('%y-%m-%d')

var1 = get_temp_var(city1, start_date, end_date)
var2 = get_temp_var(city2, start_date, end_date)

if var1 < var2:
    print(f"We choose {city1} because of less temperature variance")
else:
     print(f"We choose {city2} because of less temperature variance")