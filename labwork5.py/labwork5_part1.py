import pandas as pd
from pathlib import Path

# LOADING DATASETS
folder = Path(__file__).parent
df_students = pd.read_csv(folder / "students.csv")

#DISPLAY FIRST 5 ROWS
print(df_students.head(5))

#FIND NUMBER OF ROWS AND COLUMNS
print(df_students.shape)

#SELECT NAME AND GPA
print(df_students[["name", "GPA"]])

#FIND STUDENTS WITH GPA GREATER THAN OR EQUAL TO 3.5
print(df_students[df_students["GPA"] >= 3.5])

#SORT STUDENTS BY GPA 
print(df_students.sort_values("GPA", ascending=False)) #High -> Low
print(df_students.sort_values("GPA")) #Low -> High

#FIND AVERAGE GPA BY MAJOR
print(df_students.groupby("major")["GPA"].mean())