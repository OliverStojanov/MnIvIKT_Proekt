import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Load the dataset
data_path = r'D:\MnIvIKT_proekt\Virtual_Reality_in_Education_Impact.xlsx'
data = pd.read_excel(data_path)

# Display first few rows of the data to understand its structure
print(data.head())

# Encode 'Stress_Level_with_VR_Usage' column
data['Stress_Level_encoded'] = data['Stress_Level_with_VR_Usage'].map({'Low': 0, 'Medium': 1, 'High': 2})

# For Impact on Creativity
X_creativity = data[['Hours_of_VR_Usage_Per_Week']]
y_creativity = data['Impact_on_Creativity']
model_creativity = LinearRegression().fit(X_creativity, y_creativity)
print("Regression for Impact on Creativity:")
print("Coefficient:", model_creativity.coef_)
print("Intercept:", model_creativity.intercept_)

# For Stress (now using the encoded Stress_Level)
try:
    X_stress = data[['Hours_of_VR_Usage_Per_Week']]
    y_stress = data['Stress_Level_encoded']
    model_stress = LinearRegression().fit(X_stress, y_stress)
    print("\nRegression for Stress:")
    print("Coefficient:", model_stress.coef_)
    print("Intercept:", model_stress.intercept_)
except KeyError as e:
    print(f"Error: {e}. Ensure 'Stress_Level_encoded' is correctly named in your DataFrame.")

# For Engagement
X_engagement = data[['Hours_of_VR_Usage_Per_Week']]
y_engagement = data['Engagement_Level']
model_engagement = LinearRegression().fit(X_engagement, y_engagement)
print("\nRegression for Engagement:")
print("Coefficient:", model_engagement.coef_)
print("Intercept:", model_engagement.intercept_)
print("\n\n")

# Data
data = {
    "Metric": ["Impact on Creativity", "Stress", "Engagement"],
    "Coefficient": [model_creativity.coef_, model_stress.coef_, model_engagement.coef_],
    "Intercept": [model_creativity.intercept_, model_stress.intercept_, model_engagement.intercept_]
}

# Create DataFrame
regression_results = pd.DataFrame(data)

# Display the table
print(regression_results)


