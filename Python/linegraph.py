import pandas as pd
import matplotlib.pyplot as plt


department = {"students": ["Allison", "Morya", "El", "James", "Anton"],
              "courses": ["Math", "Physics", "Government", "General Studies", "Biology"]
}

df = pd.DataFrame(department)

plt.bar(df["students"], df["courses"])

plt.xlabel("Students")
plt.ylabel("Courses")
plt.title("Students x Courses")
plt.colorbar(cax= "red")
plt.show()