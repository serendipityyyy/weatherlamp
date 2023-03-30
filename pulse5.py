import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['LIFXAPIkey']



headers = {
    "Authorization": "Bearer %s" % TOKEN,
}

data = {
    "period": 2,
    "cycles": 5,
    "color": "green",
}

response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', data=data, headers=headers)
