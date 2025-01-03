import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

filepath = r'D:\MnIvIKT_proekt\Virtual_Reality_in_Education_Impact.xlsx'

data = pd.read_excel(filepath)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)



response_counts = data['Usage_of_VR_in_Education'].value_counts()
print(response_counts.head())

plt.figure(figsize=(8, 8))
plt.pie(
    response_counts,
    labels=response_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'lightblue']  # Optional: Adjust colors
)
plt.title('Percentage of Students Using VR in education')
plt.show()
