
import numpy as np
import pandas as pd

students = {
    "Name": ["Pooja", "Priya", "Kaviya", "Divya", "Sneha"],
    "Age": [21, 20, 21, 20, 22],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(students)

print("Student Data:")
print(df)

print("\nFirst 3 Students:")
print(df.head(3))

print("\nData Information:")
print(df.info())

marks = np.array(df["Marks"])

print("\nMarks Analysis:")
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("\nStudents Scoring Above 85:")
print(df[df["Marks"] > 85])
