import requests
import time

token = "cad51ac2161cb093ec6226896055acd362f92e39fb97da8f5b4db8efac490e22"

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

def set_lights_to_teal():
    """
    Set all lights to teal
    :return:
    """
    payload = {
        "power": "on",
        "color": "2D7F9D"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

def get_temperature():
    response = requests.get('https://api.weather.gov/gridpoints/EWX/157,100/forecast')
    temperature = response.json()['properties']['periods'][0]['temperature']
    return temperature


def set_color_from_weather_condition(temperature, precipitation):
    if precipitation > 0:
        set_lights_to_teal()
    elif precipitation == 0:
        if temperature < 66:
            set_lights_to_blue()
        elif temperature > 66:
            set_lights_to_red()
        elif temperature == 66:
            set_lights_to_purple()


def get_percent_of_precipitation():
    response = requests.get('https://api.weather.gov/gridpoints/EWX/157,100/forecast')
    precipitation = response.json()['properties']['periods'][0]['probabilityOfPrecipitation']['value']
    if precipitation == None:
        precipitation = 0
    return precipitation

temperature = get_temperature()
precipitation = get_percent_of_precipitation()
print(f"The temperature is: {temperature}, and the precipitation chance is {precipitation}")
set_color_from_weather_condition(temperature, precipitation)




