# krida/services/weather.py

import os
import requests
from typing import Optional, Dict

class WeatherService:
    """
    A service to interact with the OpenWeather API to get weather data.
    """
    def __init__(self, api_key: str):
        """
        Initializes the WeatherService with an API key.

        Args:
            api_key: The API key for the OpenWeather API.
        """
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city: str) -> Optional[Dict]:
        """
        Fetches the current weather for a specified city.

        Args:
            city: The name of the city.

        Returns:
            A dictionary containing the weather data, or None if an error occurs.
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use metric for Celsius, can be changed to 'imperial' for Fahrenheit
        }
        try:
            # Set a timeout to prevent the request from hanging indefinitely
            response = requests.get(self.base_url, params=params, timeout=10)
            # This will raise an HTTPError for bad responses (4xx or 5xx)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data for {city}: {e}")
            return None

# --- Example Usage for Testing ---
# This block will only run when you execute this script directly
if __name__ == '__main__':
    # It is a best practice to load secrets like API keys from environment variables
    # and not hardcode them in the source code.
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
    else:
        weather_service = WeatherService(api_key=api_key)
        # Test with a sample city
        city_name = 'Gwalior'
        weather_data = weather_service.get_weather(city_name)
        
        if weather_data:
            # The OpenWeather API returns a JSON object with a lot of data[4]
            # We can parse the relevant fields.
            temp = weather_data['main']['temp']
            condition = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            
            print(f"Successfully fetched weather for {city_name}:")
            print(f"  Temperature: {temp}°C")
            print(f"  Condition: {condition} ({description})")
        else:
            print(f"Could not fetch weather for {city_name}.")
