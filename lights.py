import requests

def set_lights_to_blue(token):
    """
    Set all lights to blue
    :return:
    """
    headers = {
        "Authorization": "Bearer %s" % token,
    }
    payload = {
        "power": "on",
        "color": "blue"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)


def set_lights_to_off(token):
    """
    Turn off all lights
    :return:
    """
    headers = {
        "Authorization": "Bearer %s" % token,
    }
    payload = {
        "power": "off",
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

def set_lights_to_red(token):
    """
    Set all lights to red
    :return:
    """
    headers = {
        "Authorization": "Bearer %s" % token,
    }
    payload = {
        "power": "on",
        "color": "red"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

def set_lights_to_purple(token):
    """
    Set all lights to purple
    :return:
    """
    headers = {
        "Authorization": "Bearer %s" % token,
    }
    payload = {
        "power": "on",
        "color": "purple"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)

def set_lights_to_teal(token):
    """
    Set all lights to teal
    :return:
    """
    headers = {
        "Authorization": "Bearer %s" % token,
    }
    payload = {
        "power": "on",
        "color": "2D7F9D"
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    print(response)