print('hello world')

import requests

token = "c63c17d3573e5d7898bdbcd90497498ccad22223fe8bdf0fac58db372aa097cc"

headers = {
    "Authorization": "Bearer %s" % token,
}

response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)