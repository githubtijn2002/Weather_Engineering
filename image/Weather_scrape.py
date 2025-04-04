import requests
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "17753b7913894b1a05c2927b2216a59e"
CITY = "Amstelveen"

def get_weather_data(city):
    """Fetch weather data from OpenWeatherMap API."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use metric units for temperature
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
def parse_weather_data(data):
    """Parse the weather data and extract relevant information."""
    