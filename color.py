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

def set_lights_to_red():
    """
    Set all lights to red
    :return:
    """
    payload = {
        "power": "on",
        "color": "red"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

def set_lights_to_purple():
    """
    Set all lights to purple
    :return:
    """
    payload = {
        "power": "on",
        "color": "purple"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

def get_temperature():
    response = requests.get('https://api.weather.gov/gridpoints/EWX/157,100/forecast')
    temperature = response.json()['properties']['periods'][0]['temperature']
    return temperature

def set_color_from_temp(temperature):
    if temperature < 70:
        set_lights_to_blue()
    elif temperature > 70:
        set_lights_to_red()
    elif temperature == 70:
        set_lights_to_purple()

for i in range(60, 81):
    print(f"The temperature is: {i}")
    set_color_from_temp(i)
    time.sleep(3)


