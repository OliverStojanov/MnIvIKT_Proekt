import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')

# Load the data from the Excel file
filepath = r'D:\MnIvIKT_Proekt\Virtual_Reality_in_Education_Impact.xlsx'
data = pd.read_excel(filepath)

# Group data by 'Stress_Level_with_VR_Usage' and calculate the average 'Hours_of_VR_Usage_Per_Week'
Perceived_Effectiveness_of_VR = data['Perceived_Effectiveness_of_VR'].value_counts()
print(Perceived_Effectiveness_of_VR)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    Perceived_Effectiveness_of_VR,
    labels=Perceived_Effectiveness_of_VR.index,
    autopct='%1.1f%%',  # Display percentage
    startangle=90,
    colors=['green', 'red', 'blue', 'yellow', 'orange']  # Optional: Adjust colors
)
for text in texts:
    text.set_fontsize(18)


# Title for the chart
plt.title('Distribution of Students by Perceived Effectiveness of VR')

# Show the chart
plt.show()