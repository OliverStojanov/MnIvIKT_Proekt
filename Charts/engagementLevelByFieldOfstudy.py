import pandas as pd
import matplotlib.pyplot as plt

# Load the data
filepath = r'D:\MnIvIKT proekt\Virtual_Reality_in_Education_Impact.xlsx'

data = pd.read_excel(filepath)

used_vr = data[data['Usage_of_VR_in_Education'] == 'Yes']

# Group data by 'Usage_of_VR_in_Education' and calculate the average engagement level
average_engagement = used_vr.groupby('Field_of_Study')['Engagement_Level'].mean()

# Create the bar chart
plt.figure(figsize=(8, 6))
ae = average_engagement.plot(kind='bar', color=['skyblue', 'orange'])

# Add labels and title
plt.xlabel('Field Of Study')
plt.ylabel('Average Engagement Level')
plt.title('Average Engagement Level for each Field of Study that has VR in education')
plt.xticks(rotation=0)  # Keep labels horizontal
plt.ylim(0, 5)  # Set y-axis limit to match the range of engagement levels

# Add the average engagement values on top of the bars
for i, v in enumerate(average_engagement):
    ae.text(i, v + 0.05, f'{v:.2f}', ha='center', va='bottom', fontsize=12)

# Ensure the plot fits nicely
plt.tight_layout()

# Show the chart
plt.show()