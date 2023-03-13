import requests

token = "c63c17d3573e5d7898bdbcd90497498ccad22223fe8bdf0fac58db372aa097cc"

headers = {
    "Authorization": "Bearer %s" % token,
}

payload = {
    "power": "on",
    "color": "blue"
}

response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


print(response)
