import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
filepath = r'D:\MnIvIKT proekt\Virtual_Reality_in_Education_Impact.xlsx'
data = pd.read_excel(filepath)

# Define the bins for grouping the 'Hours_of_VR_Usage_Per_Week' column
bins = [0, 2, 4, 6, 8, float('inf')]  # [0,2], [2,4], [4,6], [6,8], [>8]
labels = ['0-2', '2-4', '4-6', '6-8', '>8']

# Use pd.cut() to categorize the 'Hours_of_VR_Usage_Per_Week' into the defined bins
data['Usage_Group'] = pd.cut(data['Hours_of_VR_Usage_Per_Week'], bins=bins, labels=labels, right=False)

# Group the data by 'Usage_Group' and 'Stress_Level_with_VR_Usage' and count the number of students
grouped_data = data.groupby(['Usage_Group', 'Stress_Level_with_VR_Usage']).size().unstack(fill_value=0)

# Print the grouped data (optional)
print(grouped_data)

# Plot the grouped data as a side-by-side bar chart
ax = grouped_data.plot(kind='bar', figsize=(12, 6), width=0.8, position=1, color=['lightgreen', 'lightcoral', 'lightskyblue'])

# Add labels and title
plt.xlabel('Hours of VR Usage per Week')
plt.ylabel('Number of Students')
plt.title('Number of Students by Stress Level and Hours of VR Usage per Week')

# Add the count on top of each bar
for i in range(len(grouped_data)):
    for j, count in enumerate(grouped_data.iloc[i]):
        plt.text(i + (j - 3)*0.2, count + 0.2, str(count), ha='center', va='bottom', fontsize=10)

# Show the chart
plt.tight_layout()
plt.show()
