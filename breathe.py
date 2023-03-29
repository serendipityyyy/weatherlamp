import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['LIFXAPIkey']

headers = {
    "Authorization": "Bearer %s" % TOKEN,
}

data = {
    "period": 8,
    "cycles": 15,
    "color": "blue",
}

response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=data, headers=headers)