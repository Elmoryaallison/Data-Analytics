import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.histplot(data = tips, x= 'tip_amounts', y= 'total_bill')

plt.show()