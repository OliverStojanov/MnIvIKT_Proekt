import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')

# Load the data from the Excel file
filepath = r'D:\MnIvIKT_Proekt\Virtual_Reality_in_Education_Impact.xlsx'
data = pd.read_excel(filepath)

# Group data by 'Stress_Level_with_VR_Usage' and calculate the average 'Hours_of_VR_Usage_Per_Week'
average_engagement = data.groupby('Stress_Level_with_VR_Usage')['Hours_of_VR_Usage_Per_Week'].mean()
print(average_engagement)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    average_engagement,
    labels=average_engagement.index,
    autopct='%1.1f%%',  # Display percentage
    startangle=90,
    colors=['green', 'red', 'blue']  # Optional: Adjust colors
)
for text in texts:
    text.set_fontsize(18)

# Add average values on the pie chart
for i, wedge in enumerate(wedges):
    # Calculate the position of the text
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.radians(angle)) * wedge.r
    y = np.sin(np.radians(angle)) * wedge.r
    ax.text(
        x, y, f'Average hours: {average_engagement.iloc[i]:.2f}',
        ha='center', va='center', fontsize=12, color='black', fontweight='bold'
    )

# Title for the chart
plt.title('Average Hours of VR usage for each Stress Level')

# Show the chart
plt.show()