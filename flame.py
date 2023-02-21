import requests

token = "[[app:Token]]"

headers = {
    "Authorization": "Bearer %s" % token,
}

data = {
    "power_on": True
}

response = requests.post('https://api.lifx.com/v1/lights/all/effects/flame', data=data, headers=headers)