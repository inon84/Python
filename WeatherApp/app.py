from datetime import datetime as dt
from datetime import timezone, timedelta, tzinfo
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

#TODO: check this after fixing the client "ip_address" fetch to fetch client "city"
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
@app.route('/<city>')
def index(city=None):
    if city != None:
        #TODO: Handle errors on city name, if not 200 OK
        city=city
    else: city = "Tel Aviv"
    #TODO: fix this to get the client ip_address to fetch city
    # ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # city = get_geo(ip_address)
    
    API_KEY = 'ebb0bc77fb0c2a744c9b44d4c97b2631' # TODO: Hide in env vars?
    WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'

    now = dt.now(timezone.utc).strftime('%X | %A, %d %B, %Y')
    now_utc = dt.now(timezone.utc)
    now_local = now_utc.astimezone()

    print("now:", now)
    print("now_utc:", now_utc)
    print("now_local:", now_local)
    
    r = requests.get(WEATHER_URL.format(city, API_KEY)).json()
    forecast = requests.get(FORECAST_URL.format(city, API_KEY)).json()
    
    rweather = r['weather'][0]
    rsys = r['sys']
        
    #tz offset string
    tz = dt.utcfromtimestamp(r['timezone']).strftime('%H')
    if (int(tz) < 12):
        offset = int(tz)
        tz_show="UTC+" + str(offset)
    else:
        offset = 24-int(tz)
        tz_show="UTC-" + str(offset)
    
    print(f'offset: {offset}')
    
    weather_data = {
        'city': forecast['city']['name'],
        'offset': offset,
        'country': rsys['country'],
        'description': rweather['description'],
        'main_description': rweather['main'],
        'temperature': round(r['main']['temp']),
        'icon': rweather['icon'],
        # 'sunrise': dt.utcfromtimestamp(rsys['sunrise'] + offset).strftime('%H:%m'),
        'sunrise': dt.utcfromtimestamp((rsys['sunrise']) - offset).strftime('%H:%m'),
        'sunset': dt.utcfromtimestamp(rsys['sunset'] - offset).strftime('%H:%m'),
        'timezone': str(tz_show)
    }
    
    pop = forecast['city']['population']
    
    forecast_data = {
        'city': forecast['city'],
        'population': f'{pop:,}'
    }
    
    return render_template('index.html', now_local=now_local, 
                            now_utc=now_utc, 
                            now=now, 
                            weather=weather_data, 
                            forecast=forecast_data)

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
