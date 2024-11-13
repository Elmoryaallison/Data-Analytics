import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

file_path = r"C:\Users\admin\Documents\Data Analytics In Emblic Technologies\Excel Spreadsheet Materials\EIT data analytics material.xlsx"

df = pd.read_excel(file_path, "Data_Set 1")
# sns.barplot(data = df, x = 'Item', kde = True, color = "red")
sns.histplot(data = df, kde= True, x = "Item", y= "Units", color = 'purple')

plt.title("History of the width of the sepal")
plt.show()