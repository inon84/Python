from datetime import datetime
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
        city=city
    else: city = "Boston"
    #TODO: fix this to get the client ip_address to fetch city
    # ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # city = get_geo(ip_address)
    
    #TODO: Handle errors on city name, if not 200 OK
    API_KEY = 'ebb0bc77fb0c2a744c9b44d4c97b2631' # TODO: Hide in env vars?
    WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'

    now = datetime.now().strftime('%X | %A, %d %B, %Y')
    r = requests.get(WEATHER_URL.format(city, API_KEY)).json()
    forecast = requests.get(FORECAST_URL.format(city, API_KEY)).json()

    # weather & forecast mocks "Tel Aviv" city below, un-comment aboves and comment the belows when done:
    # r = {'coord': {'lon': 34.8, 'lat': 32.0833}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 26.08, 'feels_like': 26.08, 'temp_min': 24.6, 'temp_max': 27.14, 'pressure': 1005, 'humidity': 67}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 150}, 'clouds': {'all': 0}, 'dt': 1629410490, 'sys': {'type': 1, 'id': 6845, 'country': 'IL', 'sunrise': 1629428916, 'sunset': 1629476409}, 'timezone': 10800, 'id': 293396, 'name': 'Tel Aviv', 'cod': 200}
    
    # 5 day / 3 hour forecast data
    # forecast = {'cod': '200', 'message': 0, 'cnt': 40, 'list': [{'dt': 1629428400, 'main': {'temp': 24.78, 'feels_like': 25.14, 'temp_min': 24.78, 'temp_max': 25.51, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 1004, 'humidity': 70, 'temp_kf': -0.73}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.23, 'deg': 173, 'gust': 1.32}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-20 03:00:00'}, {'dt': 1629439200, 'main': {'temp': 26.34, 'feels_like': 26.34, 'temp_min': 26.34, 'temp_max': 27.3, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1005, 'humidity': 64, 'temp_kf': -0.96}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.28, 'deg': 224, 'gust': 1.1}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-20 06:00:00'}, {'dt': 1629450000, 'main': {'temp': 30.03, 'feels_like': 31.42, 'temp_min': 30.03, 'temp_max': 30.03, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 52, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.62, 'deg': 295, 'gust': 2.29}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-20 09:00:00'}, {'dt': 1629460800, 'main': {'temp': 30.39, 'feels_like': 32.56, 'temp_min': 30.39, 'temp_max': 30.39, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 1004, 'humidity': 55, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.95, 'deg': 310, 'gust': 3.91}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-20 12:00:00'}, {'dt': 1629471600, 'main': {'temp': 29.46, 'feels_like': 31.83, 'temp_min': 29.46, 'temp_max': 29.46, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 1004, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.3, 'deg': 336, 'gust': 5.32}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-20 15:00:00'}, {'dt': 1629482400, 'main': {'temp': 28.21, 'feels_like': 30.52, 'temp_min': 28.21, 'temp_max': 28.21, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.18, 'deg': 359, 'gust': 3.91}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-20 18:00:00'}, {'dt': 1629493200, 'main': {'temp': 27.32, 'feels_like': 29.41, 'temp_min': 27.32, 'temp_max': 27.32, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1005, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.34, 'deg': 353, 'gust': 1.71}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-20 21:00:00'}, {'dt': 1629504000, 'main': {'temp': 26.68, 'feels_like': 28.61, 'temp_min': 26.68, 'temp_max': 26.68, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1, 'deg': 8, 'gust': 1.62}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-21 00:00:00'}, {'dt': 1629514800, 'main': {'temp': 26.04, 'feels_like': 26.04, 'temp_min': 26.04, 'temp_max': 26.04, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1005, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.14, 'deg': 129, 'gust': 0.91}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-21 03:00:00'}, {'dt': 1629525600, 'main': {'temp': 28.18, 'feels_like': 30.74, 'temp_min': 28.18, 'temp_max': 28.18, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.12, 'deg': 313, 'gust': 1.58}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-21 06:00:00'}, {'dt': 1629536400, 'main': {'temp': 30.82, 'feels_like': 33.77, 'temp_min': 30.82, 'temp_max': 30.82, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 57, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.83, 'deg': 306, 'gust': 3.19}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-21 09:00:00'}, {'dt': 1629547200, 'main': {'temp': 31.43, 'feels_like': 34.74, 'temp_min': 31.43, 'temp_max': 31.43, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 56, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.69, 'deg': 323, 'gust': 5.48}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-21 12:00:00'}, {'dt': 1629558000, 'main': {'temp': 30.26, 'feels_like': 33.55, 'temp_min': 30.26, 'temp_max': 30.26, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.47, 'deg': 333, 'gust': 5.87}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-21 15:00:00'}, {'dt': 1629568800, 'main': {'temp': 28.76, 'feels_like': 31.87, 'temp_min': 28.76, 'temp_max': 28.76, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.15, 'deg': 347, 'gust': 3.87}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-21 18:00:00'}, {'dt': 1629579600, 'main': {'temp': 27.85, 'feels_like': 30.76, 'temp_min': 27.85, 'temp_max': 27.85, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 73, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.76, 'deg': 328, 'gust': 2.12}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-21 21:00:00'}, {'dt': 1629590400, 'main': {'temp': 27.18, 'feels_like': 29.74, 'temp_min': 27.18, 'temp_max': 27.18, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1005, 'humidity': 76, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.78, 'deg': 271, 'gust': 1.33}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-22 00:00:00'}, {'dt': 1629601200, 'main': {'temp': 26.77, 'feels_like': 29, 'temp_min': 26.77, 'temp_max': 26.77, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.08, 'deg': 167, 'gust': 1.38}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-22 03:00:00'}, {'dt': 1629612000, 'main': {'temp': 28.69, 'feels_like': 31.73, 'temp_min': 28.69, 'temp_max': 28.69, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.31, 'deg': 259, 'gust': 1.48}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-22 06:00:00'}, {'dt': 1629622800, 'main': {'temp': 31.05, 'feels_like': 34.46, 'temp_min': 31.05, 'temp_max': 31.05, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 58, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.95, 'deg': 301, 'gust': 4.34}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-22 09:00:00'}, {'dt': 1629633600, 'main': {'temp': 31.16, 'feels_like': 34.93, 'temp_min': 31.16, 'temp_max': 31.16, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 59, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.7, 'deg': 310, 'gust': 5.53}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-22 12:00:00'}, {'dt': 1629644400, 'main': {'temp': 29.89, 'feels_like': 33.22, 'temp_min': 29.89, 'temp_max': 29.89, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.65, 'deg': 319, 'gust': 6.22}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-22 15:00:00'}, {'dt': 1629655200, 'main': {'temp': 28.54, 'feels_like': 31.43, 'temp_min': 28.54, 'temp_max': 28.54, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.39, 'deg': 322, 'gust': 4.15}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-22 18:00:00'}, {'dt': 1629666000, 'main': {'temp': 27.96, 'feels_like': 30.46, 'temp_min': 27.96, 'temp_max': 27.96, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 69, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.7, 'deg': 302, 'gust': 3.02}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-22 21:00:00'}, {'dt': 1629676800, 'main': {'temp': 27.27, 'feels_like': 29.42, 'temp_min': 27.27, 'temp_max': 27.27, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.13, 'deg': 302, 'gust': 2.41}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-23 00:00:00'}, {'dt': 1629687600, 'main': {'temp': 26.65, 'feels_like': 26.65, 'temp_min': 26.65, 'temp_max': 26.65, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.25, 'deg': 280, 'gust': 1.68}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-23 03:00:00'}, {'dt': 1629698400, 'main': {'temp': 28.24, 'feels_like': 30.31, 'temp_min': 28.24, 'temp_max': 28.24, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.36, 'deg': 250, 'gust': 2.13}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-23 06:00:00'}, {'dt': 1629709200, 'main': {'temp': 30.2, 'feels_like': 32.04, 'temp_min': 30.2, 'temp_max': 30.2, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 54, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.73, 'deg': 280, 'gust': 3.57}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-23 09:00:00'}, {'dt': 1629720000, 'main': {'temp': 30.4, 'feels_like': 32.38, 'temp_min': 30.4, 'temp_max': 30.4, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 54, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.98, 'deg': 297, 'gust': 3.97}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-23 12:00:00'}, {'dt': 1629730800, 'main': {'temp': 29.15, 'feels_like': 30.98, 'temp_min': 29.15, 'temp_max': 29.15, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1005, 'humidity': 58, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.21, 'deg': 314, 'gust': 3.87}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-23 15:00:00'}, {'dt': 1629741600, 'main': {'temp': 27.77, 'feels_like': 29.43, 'temp_min': 27.77, 'temp_max': 27.77, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.07, 'deg': 327, 'gust': 2.17}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-23 18:00:00'}, {'dt': 1629752400, 'main': {'temp': 26.94, 'feels_like': 28.44, 'temp_min': 26.94, 'temp_max': 26.94, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1006, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.85, 'deg': 331, 'gust': 1.03}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-23 21:00:00'}, {'dt': 1629763200, 'main': {'temp': 26.09, 'feels_like': 26.09, 'temp_min': 26.09, 'temp_max': 26.09, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 69, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.44, 'deg': 254, 'gust': 1.59}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-24 00:00:00'}, {'dt': 1629774000, 'main': {'temp': 25.6, 'feels_like': 26.04, 'temp_min': 25.6, 'temp_max': 25.6, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.44, 'deg': 216, 'gust': 1.92}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-24 03:00:00'}, {'dt': 1629784800, 'main': {'temp': 27.58, 'feels_like': 28.85, 'temp_min': 27.58, 'temp_max': 27.58, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1007, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.4, 'deg': 205, 'gust': 2.54}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-24 06:00:00'}, {'dt': 1629795600, 'main': {'temp': 30.26, 'feels_like': 30.96, 'temp_min': 30.26, 'temp_max': 30.26, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 47, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.98, 'deg': 267, 'gust': 3.05}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-24 09:00:00'}, {'dt': 1629806400, 'main': {'temp': 30.3, 'feels_like': 31.17, 'temp_min': 30.3, 'temp_max': 30.3, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 48, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.64, 'deg': 295, 'gust': 3.45}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-24 12:00:00'}, {'dt': 1629817200, 'main': {'temp': 29.1, 'feels_like': 30.05, 'temp_min': 29.1, 'temp_max': 29.1, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 52, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.9, 'deg': 314, 'gust': 3.26}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-24 15:00:00'}, {'dt': 1629828000, 'main': {'temp': 27.5, 'feels_like': 28.56, 'temp_min': 27.5, 'temp_max': 27.5, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 58, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.95, 'deg': 352, 'gust': 1.98}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2021-08-24 18:00:00'}, {'dt': 1629838800, 'main': {'temp': 26.72, 'feels_like': 27.74, 'temp_min': 26.72, 'temp_max': 26.72, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.9, 'deg': 34, 'gust': 1.99}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-24 21:00:00'}, {'dt': 1629849600, 'main': {'temp': 25.88, 'feels_like': 26.12, 'temp_min': 25.88, 'temp_max': 25.88, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1006, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 0.77, 'deg': 339, 'gust': 0.93}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2021-08-25 00:00:00'}], 'city': {'id': 293396, 'name': 'Tel Aviv', 'coord': {'lat': 32.0833, 'lon': 34.8}, 'country': 'IL', 'population': 1221600, 'timezone': 10800, 'sunrise': 1629428916, 'sunset': 1629476409}}
    
    rweather = r['weather'][0]
    rsys = r['sys']
    
    tz = datetime.utcfromtimestamp(r['timezone']).strftime('%H')
    if (int(tz) < 12):
        tz="UTC+" + tz
    else:
        tz="UTC-" + str(24-int(tz))
    
    weather_data = {
        'city': city,
        'country': rsys['country'],
        'description': rweather['description'],
        'main_description': rweather['main'],
        'temperature': round(r['main']['temp']),
        'icon': rweather['icon'],
        'sunrise': datetime.fromtimestamp(rsys['sunrise']).strftime('%H:%m'),
        'sunset': datetime.fromtimestamp(rsys['sunset']).strftime('%H:%m'),
        'timezone': tz
    }
    
    pop = forecast['city']['population']
    
    forecast_data = {
        'city': city,
        'population': f'{pop:,}'
    }
    
    return render_template('index.html', now=now, weather=weather_data, forecast=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
