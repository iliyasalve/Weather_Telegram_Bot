from config import api_key

import requests
import datetime 

def city_info(city: str, api: str) -> dict:
    '''
    Returns a dictionary that stores the name of the city and country in English, as well as the coordinates of the city
    '''

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api}'

    info = requests.get(url).json()

    city_info_dict = {}

    city_info_dict['city_name'] = info[0]['name']
    city_info_dict['country'] = info[0]['country']

    city_info_dict['lat'] = info[0]['lat']
    city_info_dict['lon'] = info[0]['lon']

    return city_info_dict


def weather_info(lat: float, lon: float) -> dict:
    '''
    Returns a dictionary that stores all the necessary information about the weather in the selected city:

    Full API documentation: https://openweathermap.org/current
    '''

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'

    current_weather = requests.get(url).json()

    weather_info_dict = {}

    weather_info_dict['description'] = current_weather['weather'][0]['description']

    weather_info_dict['icon'] = current_weather['weather'][0]['icon']

    weather_info_dict['temperature'] = round(current_weather['main']['temp'])
    weather_info_dict['feels_like'] = round(current_weather['main']['feels_like'])
    weather_info_dict['temperature_min'] = round(current_weather['main']['temp_min'])
    weather_info_dict['temperature_max'] = round(current_weather['main']['temp_max'])

    weather_info_dict['pressure'] = current_weather['main']['pressure']
    weather_info_dict['humidity'] = current_weather['main']['humidity']

    weather_info_dict['wind_speed'] = current_weather['wind']['speed']

    weather_info_dict['visibility'] = current_weather['visibility']/1000

    weather_info_dict['sunrise'] = datetime.datetime.fromtimestamp(current_weather['sys']['sunrise'] ).strftime('%H:%M:%S')
    weather_info_dict['sunset'] = datetime.datetime.fromtimestamp(current_weather['sys']['sunset'] ).strftime('%H:%M:%S')

    return weather_info_dict


def weather_message(city: str) -> tuple[str, str]:
    '''
    Returns a message about the weather in the selected city in English, as well as a weather icon
    '''

    city_info_dict = city_info(city, api_key)

    weather_info_dict = weather_info(city_info_dict['lat'], city_info_dict['lon'])

    message = f'Information about the weather in the city of **{city_info_dict['city_name']} ({city_info_dict['country']})** by this time:\n' \
                f'\n' \
                f'_{weather_info_dict['description'].capitalize()}_\n\n' \
                f'🌡️ Temperature: {weather_info_dict['temperature']}°C\n' \
                f'🌡️ Feels like: {weather_info_dict['feels_like']}°C\n' \
                f'🌡️ Minimum temperature: {weather_info_dict['temperature_min']}°C\n' \
                f'🌡️ Maximum temperature: {weather_info_dict['temperature_max']}°C\n' \
                f'\n' \
                f'🗜 Pressure: {weather_info_dict['pressure']} millibars\n' \
                f'💧 Humidity: {weather_info_dict['humidity']}%\n' \
                f'\n' \
                f'💨 Wind speed: {weather_info_dict['wind_speed']} meter/sec\n' \
                f'\n' \
                f'👀 Visibility: {weather_info_dict['visibility']} km\n' \
                f'\n' \
                f'🌅 Sunrise: {weather_info_dict['sunrise']}\n' \
                f'🌅 Sunset: {weather_info_dict['sunset']}\n'
    
    icon = f'https://openweathermap.org/img/wn/{weather_info_dict['icon']}@2x.png'

    return message, icon

