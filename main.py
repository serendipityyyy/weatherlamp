import time
import configparser
from lights import set_lights_to_blue
from lights import set_lights_to_off
from lights import set_lights_to_red
from lights import set_lights_to_purple
from lights import set_lights_to_teal
from weather import get_temperature
from weather import get_percent_of_precipitation


config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['LIFXAPIkey']
WEATHER_STATION = config['WEATHER']['Station']
WEATHER_LATITUDE = config['WEATHER']["Latitude"]
WEATHER_LONGITUDE = config['WEATHER']['Longitude']


def set_color_from_weather_condition(temperature, precipitation):
    if precipitation > 0:
        set_lights_to_teal(TOKEN)
    elif precipitation == 0:
        if temperature < 66:
            set_lights_to_blue(TOKEN)
        elif temperature > 66:
            set_lights_to_red(TOKEN)
        elif temperature == 66:
            set_lights_to_purple(TOKEN)


temperature = get_temperature(WEATHER_STATION, WEATHER_LATITUDE, WEATHER_LONGITUDE)
precipitation = get_percent_of_precipitation(WEATHER_STATION, WEATHER_LATITUDE, WEATHER_LONGITUDE)
print(f"The temperature is: {temperature}, and the precipitation chance is {precipitation}")
set_color_from_weather_condition(temperature, precipitation)
time.sleep(5)
set_lights_to_off(TOKEN)
