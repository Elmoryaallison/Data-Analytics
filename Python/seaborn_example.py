import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Working with Iris dataset

iris = sns.load_dataset("iris")

sns.histplot(data = iris, x = "sepal_width", kde  = True, color = "Purple")

plt.title("History of the Width of the sepal")
plt.show()