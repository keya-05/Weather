import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report
# Load data from CSV
data = pd.read_csv('weather_data.csv')

# Convert weather conditions to numerical values for classification
data['weather_condition'] = data['weather_condition'].map({
    'Sunny': 0, 'Cloudy': 1, 'Rainy': 2
})

# Regression: Predict temperature
X_temp = data[['moisture_index', 'wind_speed']]  # Features
y_temp = data['temperature']  # Target

X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(X_temp, y_temp, test_size=0.2, random_state=42)

# Train Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train_temp, y_train_temp)

# Predictions and MSE
y_pred_temp = linear_model.predict(X_test_temp)
mse = mean_squared_error(y_test_temp, y_pred_temp)
print(f"Linear Regression MSE: {mse}")

# Classification: Predict weather conditions
X_weather = data[['moisture_index', 'wind_speed']]
y_weather = data['weather_condition']

X_train_weather, X_test_weather, y_train_weather, y_test_weather = train_test_split(X_weather, y_weather, test_size=0.2, random_state=42)

# Train Decision Tree and Random Forest models
dt_model = DecisionTreeClassifier()
rf_model = RandomForestClassifier()

dt_model.fit(X_train_weather, y_train_weather)
rf_model.fit(X_train_weather, y_train_weather)

# Decision Tree Predictions
y_pred_weather_dt = dt_model.predict(X_test_weather)
print("Decision Tree Classification Report:")
print(classification_report(y_test_weather, y_pred_weather_dt, target_names=['Sunny', 'Cloudy', 'Rainy']))

# Random Forest Predictions
y_pred_weather_rf = rf_model.predict(X_test_weather)
print("Random Forest Classification Report:")
print(classification_report(y_test_weather, y_pred_weather_rf, target_names=['Sunny', 'Cloudy', 'Rainy']))
