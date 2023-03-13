import requests
import time

token = "c63c17d3573e5d7898bdbcd90497498ccad22223fe8bdf0fac58db372aa097cc"

headers = {
    "Authorization": "Bearer %s" % token,
}

def set_lights_to_blue():
    """
    Set all lights to blue
    :return:
    """
    payload = {
        "power": "on",
        "color": "blue"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)


def set_lights_to_off():
    """
    Turn off all lights
    :return:
    """
    payload = {
        "power": "off",
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

while True:
    set_lights_to_blue()
    time.sleep(2)
    set_lights_to_off()
    time.sleep(2)
