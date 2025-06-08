import os
import requests
from typing import Optional, Dict

class WeatherService:
    """A service to interact with the OpenWeather API to get weather data."""
    
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
            'units': 'metric'  # Change to 'imperial' for Fahrenheit
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

if __name__ == '__main__':
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
    else:
        weather_service = WeatherService(api_key=api_key)
        # Test with a sample city
        city_name = 'Gwalior'
        weather_data = weather_service.get_weather(city_name)
        
        if weather_data:
            temp = weather_data['main']['temp']
            condition = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            
            print(f"Successfully fetched weather for {city_name}:")
            print(f"  Temperature: {temp}°C")
            print(f"  Condition: {condition} ({description})")
        else:
            print(f"Could not fetch weather for {city_name}.")
