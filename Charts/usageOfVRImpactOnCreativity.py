import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

# Load the data
filepath = r'D:\MnIvIKT_Proekt\Virtual_Reality_in_Education_Impact.xlsx'

data = pd.read_excel(filepath)

# Group data by 'Usage_of_VR_in_Education' and calculate the average engagement level
average_creativity = data.groupby('Usage_of_VR_in_Education')['Impact_on_Creativity'].mean()

# Create the bar chart
plt.figure(figsize=(8, 6))
ae = average_creativity.plot(kind='bar', color=['skyblue', 'orange'])

# Add labels and title
plt.xlabel('Usage of VR in Education')
plt.ylabel('Average Creativity Level')
plt.title('Average Creativity Level by VR Usage')
plt.xticks(rotation=0)  # Keep labels horizontal
plt.ylim(0, 5)  # Set y-axis limit to match the range of engagement levels

# Add the average engagement values on top of the bars
for i, v in enumerate(average_creativity):
    ae.text(i, v + 0.05, f'{v:.2f}', ha='center', va='bottom', fontsize=12)

# Ensure the plot fits nicely
plt.tight_layout()

# Show the chart
plt.show()