import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, classification_report
# Sample data (replace with your actual dataset)
data = pd.DataFrame({
    'temperature': [20, 21, 19, 22, 25, 24, 23, 26, 22, 21],
    'humidity': [60, 55, 70, 65, 75, 80, 85, 90, 95, 100],
    'wind_speed': [5, 7, 6, 8, 10, 5, 4, 9, 7, 6],
    'weather_condition': ['sunny', 'sunny', 'cloudy', 'rainy', 'sunny', 'rainy', 'cloudy', 'sunny', 'cloudy', 'rainy']
})

# Step 1: Preparing data for Linear Regression
X_temp = data[['humidity', 'wind_speed']]  # Features for regression
y_temp = data['temperature']  # Target for regression

# Step 2: Train-Test Split
X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(X_temp, y_temp, test_size=0.2, random_state=42)

# Step 3: Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X_train_temp, y_train_temp)

# Predictions
y_pred_temp = linear_model.predict(X_test_temp)
mse = mean_squared_error(y_test_temp, y_pred_temp)
print(f"Linear Regression MSE: {mse}")

# Step 4: Preparing data for Weather Classification
# Encode weather conditions as integers
data['weather_condition'] = data['weather_condition'].map({'sunny': 0, 'cloudy': 1, 'rainy': 2})
X_weather = data[['humidity', 'wind_speed']]  # Features for classification
y_weather = data['weather_condition']  # Target for classification

# Train-Test Split for classification
X_train_weather, X_test_weather, y_train_weather, y_test_weather = train_test_split(X_weather, y_weather, test_size=0.2, random_state=42)

# Step 5: Decision Tree Classifier
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train_weather, y_train_weather)

# Predictions
y_pred_weather_dt = dt_model.predict(X_test_weather)
print("Decision Tree Classification Report:")
print(classification_report(y_test_weather, y_pred_weather_dt, target_names=['sunny', 'cloudy', 'rainy']))

# Step 6: Random Forest Classifier
rf_model = RandomForestClassifier()
rf_model.fit(X_train_weather, y_train_weather)

# Predictions
y_pred_weather_rf = rf_model.predict(X_test_weather)
print("Random Forest Classification Report:")
print(classification_report(y_test_weather, y_pred_weather_rf, target_names=['sunny', 'cloudy', 'rainy']))
