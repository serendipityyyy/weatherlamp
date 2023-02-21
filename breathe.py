import requests

token = "cad51ac2161cb093ec6226896055acd362f92e39fb97da8f5b4db8efac490e22"

headers = {
    "Authorization": "Bearer %s" % token,
}

data = {
    "period": 2,
    "cycles": 5,
    "color": "green",
}

response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=data, headers=headers)