import requests

def get_temperature(weather_station, weather_latitude, weather_longitude):
    response = requests.get(f"https://api.weather.gov/gridpoints/{weather_station}/{weather_latitude},{weather_longitude}/forecast")
    temperature = response.json()['properties']['periods'][0]['temperature']
    return temperature

def get_percent_of_precipitation(weather_station, weather_latitude, weather_longitude):
    response = requests.get(f'https://api.weather.gov/gridpoints/{weather_station}/{weather_latitude},{weather_longitude}/forecast')
    precipitation = response.json()['properties']['periods'][0]['probabilityOfPrecipitation']['value']
    if precipitation == None:
        precipitation = 0
    return precipitation
