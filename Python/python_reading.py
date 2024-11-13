import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\admin\Documents\Data Analytics In Emblic Technologies\Excel Spreadsheet Materials\EIT data analytics material.xlsx"

df = pd.read_excel(file_path, "Data_Set 1")

df.drop_duplicates(inplace = True)
plt.bar(df["Item"], df["Units"])
plt.xlabel("Items")
plt.ylabel("Total Cost")
# plt.show()
# print(df.to_string(index= False))
# print(df.isnull().sum())
# print(df.head())
# print(df["Item"].head(20))

print(df[["Item", "Units"]])
# f1 = df["Item"] == "Pencil"
# f2 = df["Item"] == "Pen"

# print(df[f1 | f2])

