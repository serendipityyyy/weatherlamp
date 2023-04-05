import requests
import time
import configparser
from lights import set_lights_to_blue
from lights import set_lights_to_off
from lights import set_lights_to_red
from lights import set_lights_to_purple
from lights import set_lights_to_teal
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['LIFXAPIkey']
WEATHER_STATION = config['WEATHER']['Station']
WEATHER_LATITUDE = config['WEATHER']["Latitude"]
WEATHER_LONGITUDE = config['WEATHER']['Longitude']

headers = {
    "Authorization": "Bearer %s" % TOKEN,
}


def get_temperature():
    response = requests.get(f"https://api.weather.gov/gridpoints/{WEATHER_STATION}/{WEATHER_LATITUDE},{WEATHER_LONGITUDE}/forecast")
    temperature = response.json()['properties']['periods'][0]['temperature']
    return temperature


def set_color_from_weather_condition(temperature, precipitation):
    if precipitation > 0:
        set_lights_to_teal()
    elif precipitation == 0:
        if temperature < 66:
            set_lights_to_blue(TOKEN)
        elif temperature > 66:
            set_lights_to_red()
        elif temperature == 66:
            set_lights_to_purple()



def get_percent_of_precipitation():
    response = requests.get(f'https://api.weather.gov/gridpoints/{WEATHER_STATION}/{WEATHER_LATITUDE},{WEATHER_LONGITUDE}/forecast')
    precipitation = response.json()['properties']['periods'][0]['probabilityOfPrecipitation']['value']
    if precipitation == None:
        precipitation = 0
    return precipitation

temperature = get_temperature()
precipitation = get_percent_of_precipitation()
print(f"The temperature is: {temperature}, and the precipitation chance is {precipitation}")
set_color_from_weather_condition(temperature, precipitation)
time.sleep(5)
set_lights_to_off()




