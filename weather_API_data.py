import requests
import time
API_KEY = 'b3fd8d4d0ec74159a4960737241610'  
BASE_URL = 'https://api.weatherapi.com/v1/current.json'
def fetch_weather_data(city):
    params = {
        'key': API_KEY,  
        'q': city,
        'aqi': 'no' 
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['current']['temp_c'],  
            'moisture_index': data['current']['humidity'],  
            'wind_speed': data['current']['wind_kph'],  
            'atmospheric_pressure': data['current']['pressure_mb'] 
        }
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
# Example city for testing
city = 'London'  
while True:
    weather_data = fetch_weather_data(city)
    if weather_data:
        print(f"Weather data for {city}: {weather_data}")
    time.sleep(60) 
