import pandas as pd
import matplotlib.pyplot as plt

filepath = r'D:\MnIvIKT proekt\Virtual_Reality_in_Education_Impact.xlsx'

data = pd.read_excel(filepath)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

used_vr = data[data['Usage_of_VR_in_Education'] == 'Yes']
print(used_vr.head())

response_counts = used_vr['Improvement_in_Learning_Outcomes'].value_counts()
print(response_counts.head())

plt.figure(figsize=(8, 8))
plt.pie(
    response_counts,
    labels=response_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'salmon']  # Optional: Adjust colors
)
plt.title('Impact of VR on Learning Outcomes')
plt.show()





# usage_of_VR_in_Education = data['Usage_of_VR_in_Education']  # Replace with the actual column name for categories
# improvement_in_Learning_Outcomes = data['Improvement_in_Learning_Outcomes']     # Replace with the column you want to plot
#
# plt.figure(figsize=(10, 6))
# plt.bar(x, y, color='skyblue')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Chart Example')
# plt.xticks(rotation=45)
# plt.tight_layout()  # Ensures labels fit nicely
# plt.show()