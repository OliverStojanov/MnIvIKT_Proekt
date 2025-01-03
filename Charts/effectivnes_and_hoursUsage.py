import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


data_path = r'D:\MnIvIKT_Proekt\Virtual_Reality_in_Education_Impact.xlsx'
data = pd.read_excel(data_path)

bins = [0, 3, 7, 10]  # 1-3, 4-7, 8-10
labels = ['1-3', '4-7', '8-10']  # Corresponding group labels

data['VR_Usage_Group'] = pd.cut(data['Hours_of_VR_Usage_Per_Week'], bins=bins, labels=labels, right=False)

group_averages = data.groupby('VR_Usage_Group')['Perceived_Effectiveness_of_VR'].mean()

plt.figure(figsize=(10, 6))
group_averages.plot(kind='line', marker='o', linestyle='-', color='b', markerfacecolor='c', markersize=8, linewidth=2, markeredgewidth=1)

plt.title('Average Perceived Effectiveness of VR by Usage Group')
plt.xlabel('Hours of VR Usage Per Week Group')
plt.ylabel('Average Perceived Effectiveness of VR')
plt.xticks(rotation=0) 
plt.grid(True, linestyle='--', alpha=0.5)  
plt.show()
print(group_averages)
