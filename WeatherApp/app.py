from datetime import datetime as dt
from datetime import timezone, timedelta, tzinfo
import requests
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

#TODO: check this after fixing the client "ip_address" to fetch client "city"
# def get_geo(ip_address):
#     try:
#         response = requests.get("http://api.ipstack.com/{}?access_key=053d8fb4ec21e556609a665c5006937a".format(ip_address))
#         print(response.json())
#         js = response.json()
#         city = js['city']
#         return city
#     except Exception as e:
#         return "Unknown"

@app.route('/')
@app.route('/search', methods=['POST', 'GET'])
def index(city=None):
    if request.method == 'GET':
        city = request.args.get('city')
        if city == None:
            city = "Tel Aviv"
    # if request.method == 'POST':
    #     if city != None:
    #         city = city
    #     else:
    #         city = 'Tel Aviv'
    
    #TODO: fix this to get the client ip_address to fetch city
    # ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # city = get_geo(ip_address)
    
    # FORECAST_URL (FULL URL for mocks) https://api.openweathermap.org/data/2.5/weather?q=Las%20Vegas&appid=ebb0bc77fb0c2a744c9b44d4c97b2631&units=metric
    
    API_KEY = 'ebb0bc77fb0c2a744c9b44d4c97b2631' # TODO: Hide in ENV Vars
    WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'

    now = dt.now(timezone.utc).strftime('%X | %A, %d %B, %Y')
    now_utc = dt.now(timezone.utc)
    now_local = now_utc.astimezone()

    # print("now:", now)
    # print("now_utc:", now_utc)
    # print("now_local:", now_local)
    # print(dt.fromtimestamp(1629514800))
    
    r = requests.get(WEATHER_URL.format(city, API_KEY)).json()
    forecast = requests.get(FORECAST_URL.format(city, API_KEY)).json()

    #TODO: handle bad requests
    # if r['cod'] != 200:
    #     print("bad request")
    
    rweather = r['weather'][0]
    rsys = r['sys']
        
    #tz offset string
    offset = int(dt.utcfromtimestamp(r['timezone']).strftime('%H'))
    # offset = dt(r['timezone'])
    if offset < 12:
        tz_show="UTC+" + str(offset)
    else:
        tz_show="UTC-" + str(offset)
    
    print(f'offset: {offset}')
    
    weather_data = {
        'city': forecast['city']['name'],
        'offset': int(offset),
        'country': rsys['country'],
        'description': rweather['description'],
        'main_description': rweather['main'],
        'temperature': round(r['main']['temp']),
        'icon': rweather['icon'],
        # 'sunrise': dt.utcfromtimestamp(rsys['sunrise'] + offset).strftime('%H:%m'),
        'sunrise': dt.utcfromtimestamp((rsys['sunrise']) + offset).strftime('%H:%m'),
        'sunset': dt.utcfromtimestamp(rsys['sunset'] + offset).strftime('%H:%m'),
        'timezone': str(tz_show)
    }
    
    # forecast_days = []
    # for cast in forecast['list']:
    #     forecast_days.append(cast['dt_txt'])   
    # print(forecast_days)
    
    daily_forecast = []
    daily_times = []
    
    for cast in forecast['list']:
        print(cast)
        # forecast['list'].update({cast[]})
        daily_times.append(cast['dt'])
        daily_forecast.append(cast)
            
    print(daily_forecast)
    print(daily_times)
    
    pop = forecast['city']['population']
    
    forecast_data = {
        'city': forecast['city'],
        'population': f'{pop:,}',
        'forecastlist': forecast['list']
        # 'daily_forecast': daily_forecast
        # 'days': daily_forecast['dt']
    }
    
    return render_template('index.html',
                            city=city,
                            now_local=now_local, 
                            now_utc=now_utc, 
                            now=now, 
                            weather=weather_data, 
                            daily_forecast=daily_forecast,
                            daily_times=daily_times,
                            forecast_data=forecast_data)

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
