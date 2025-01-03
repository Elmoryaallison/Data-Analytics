import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("newdata.csv")

print(df.head(11))
print(df.dtypes)
print(df.info())
print(df.describe())

sns.pairplot(df)
plt.show()