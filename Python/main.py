import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Task Sales.xlsx")

# df = pd.read_csv("newdata.csv")

# print(df.isnull().sum())

# print(df.fillna(value = 0, inplace = True))

# print(df.drop_duplicates(inplace = True))

sns.pairplot(df)
plt.show()
