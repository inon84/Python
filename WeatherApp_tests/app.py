from datetime import datetime as dt
import pytz
import requests
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/search', methods=['GET'])
def index(city=None):
    city = request.args.get('city')
    if city == None:
        city = 'Tel Aviv'
    
    # FORECAST_URL (FULL URL for mocks) https://api.openweathermap.org/data/2.5/weather?q=Las%20Vegas&appid=ebb0bc77fb0c2a744c9b44d4c97b2631&units=metric
    API_KEY = 'ebb0bc77fb0c2a744c9b44d4c97b2631' # TODO: Hide in ENV Vars
    WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'

    dt_to_check = 1629428400
    dt_text = dt.fromtimestamp(dt_to_check).astimezone(pytz.UTC)
    print('dt_text', dt_text)
    now_utc = dt.now(pytz.UTC)
    print('now_utc', now_utc)
    # return f'now_utc: {str(now_utc)}'

    weather = requests.get(WEATHER_URL.format(city, API_KEY)).json()
    forecast = requests.get(FORECAST_URL.format(city, API_KEY)).json()
    
    # class WeatherData():
    #     city = forecast['city']['name']

    # return(WeatherData.city)
    return render_template('layout.html',
                            now_utc=now_utc, weather=weather, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
