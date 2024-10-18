import weather_API_data
import weather_model
import sql_weather
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# Predict future temperature based on real-time data
new_data = fetch_weather_data('London')
real_time_input = pd.DataFrame([new_data], columns=['moisture_index', 'wind_speed'])

# Temperature prediction using linear regression
predicted_temp = linear_model.predict(real_time_input)
print(f"Predicted Temperature: {predicted_temp[0]}")

# Weather condition classification
predicted_weather = rf_model.predict(real_time_input)
weather_map = {0: 'Sunny', 1: 'Cloudy', 2: 'Rainy'}
print(f"Predicted Weather: {weather_map[predicted_weather[0]]}")
