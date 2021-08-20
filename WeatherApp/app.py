from datetime import datetime
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_geo(ip_address):
    try:
        response = requests.get("http://api.ipstack.com/{}?access_key=053d8fb4ec21e556609a665c5006937a".format(ip_address))
        print(response.json())
        js = response.json()
        city = js['city']
        return city
    except Exception as e:
        return "Unknown"

@app.route('/')
@app.route('/<city>')
def index():
    ip_address = request.remote_addr
    city = get_geo(ip_address)
    print(city)
    city='Tel Aviv'
    API_KEY = 'ebb0bc77fb0c2a744c9b44d4c97b2631'
    WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    now = datetime.now().strftime('%X | %A, %d %B, %Y')
    # r = requests.get(WEATHER_URL.format(city, API_KEY)).json()
    # weathr mock, un-comment above 'r' and comment the below 'r' when done:
    r = {'coord': {'lon': 34.8, 'lat': 32.0833}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 26.08, 'feels_like': 26.08, 'temp_min': 24.6, 'temp_max': 27.14, 'pressure': 1005, 'humidity': 67}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 150}, 'clouds': {'all': 0}, 'dt': 1629410490, 'sys': {'type': 1, 'id': 6845, 'country': 'IL', 'sunrise': 1629428916, 'sunset': 1629476409}, 'timezone': 10800, 'id': 293396, 'name': 'Tel Aviv', 'cod': 200}
    
    # print(r)
    
    weather_data = {
        'city': city,
        'country': r['sys']['country'],
        'description': r['weather'][0]['description'],
        'main_description' : r['weather'][0]['main'],
        'temprature': round(r['main']['temp']),
        'icon': r['weather'][0]['icon'],
        'sunrise': datetime.utcfromtimestamp(r['sys']['sunrise']).strftime('%H:%m'),
        'sunset': datetime.utcfromtimestamp(r['sys']['sunset']).strftime('%H:%m')
    }
    
    # print(weather_data)
    
    return render_template('index.html', now=now, weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
