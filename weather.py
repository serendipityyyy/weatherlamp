import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['LIFXAPIkey']
WEATHER_STATION = config['WEATHER']['Station']
WEATHER_LATITUDE = config['WEATHER']["Latitude"]
WEATHER_LONGITUDE = config['WEATHER']['Longitude']

def get_temperature():
    response = requests.get('https://api.weather.gov/gridpoints/{WEATHER_STATION}/{WEATHER_LATITUDE},{WEATHER_LONGITUDE}/forecast')
    temperature = response.json()['properties']['periods'][0]['temperature']
    return temperature


temperature = get_temperature()
print(temperature)