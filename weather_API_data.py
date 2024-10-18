import requests
import time
import pandas as pd
import os

# API Key and URL
API_KEY = 'b3fd8d4d0ec74159a4960737241610'
BASE_URL = 'https://api.weatherapi.com/v1/current.json'

# CSV file to store weather data
file_name = 'weather_data.csv'

# Function to fetch and store real-time weather data
def fetch_weather_data(city):
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'temperature': data['current']['temp_c'],
            'moisture_index': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
            'atmospheric_pressure': data['current']['pressure_mb'],
            'weather_condition': data['current']['condition']['text'],
            'time': data['location']['localtime']
        }
        return weather_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Save the fetched data to a CSV file
def save_to_csv(data, file_name):
    df = pd.DataFrame([data])
    if not os.path.isfile(file_name):
        df.to_csv(file_name, mode='a', header=True, index=False)
    else:
        df.to_csv(file_name, mode='a', header=False, index=False)

city = 'Delhi'
while True:
    weather_data = fetch_weather_data(city)
    if weather_data:
        print(f"Weather data: {weather_data}")
        save_to_csv(weather_data, file_name)
    time.sleep(3600)  # Fetch every 1 hour
