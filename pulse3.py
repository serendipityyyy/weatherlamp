import requests

token = "[[app:Token]]"

headers = {
    "Authorization": "Bearer %s" % token,
}

data = {
    "period": 2,
    "cycles": 5,
    "color": "green",
}

response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', data=data, headers=headers)