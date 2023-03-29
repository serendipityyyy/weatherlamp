import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['LIFXAPIkey']
WEATHER_STATION = config['WEATHER']['Station']
WEATHER_LATITUDE = config['WEATHER']["Latitude"]
WEATHER_LONGITUDE = config['WEATHER']['Longitude']



headers = {
    "Authorization": "Bearer %s" % TOKEN,
}

data = {
    "power_on": True
}

response = requests.post('https://api.lifx.com/v1/lights/all/effects/flame', data=data, headers=headers)