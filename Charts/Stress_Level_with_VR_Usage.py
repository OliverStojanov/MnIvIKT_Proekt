import pandas as pd
import matplotlib.pyplot as plt

filepath = r'D:\MnIvIKT proekt\Virtual_Reality_in_Education_Impact.xlsx'

data = pd.read_excel(filepath)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

used_vr = data[data['Usage_of_VR_in_Education'] == 'Yes']
print(used_vr.head())

response_counts = used_vr['Stress_Level_with_VR_Usage'].value_counts()
print(response_counts.head())

plt.figure(figsize=(8, 8))
plt.pie(
    response_counts,
    labels=response_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['grey', 'red', 'blue']  # Optional: Adjust colors
)
plt.title('Impact of VR on Stress Level')
plt.show()