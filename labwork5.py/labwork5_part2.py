import pandas as pd
from pathlib import Path

# LOADING DATASETS
folder = Path(__file__).parent

df_students = pd.read_csv(folder / "students.csv")
df_scores = pd.read_csv(folder / "scores.csv")

#CHECK MISSING VALUES
print(df_students.isna().sum())
print(df_scores.isna().sum())

#FILL MISSING VALUES
df_students["age"].fillna(df_students["age"].mean(), inplace=True)
df_students["GPA"].fillna(df_students["GPA"].mean(), inplace=True)
df_scores["math"].fillna(df_scores["math"].mean(), inplace=True)
df_scores["database"].fillna(df_scores["database"].mean(), inplace=True)

#REMOVE MISSING VALUES
"""
df_students["age"].dropna(df_students["age"].mean(), inplace=True)
df_students["GPA"].dropna(df_students["GPA"].mean(), inplace=True)
df_scores["math"].dropna(df_scores["math"].mean(), inplace=True)
df_scores["database"].dropna(df_scores["database"].mean(), inplace=True) 
"""

#MERGE THE TWO DATASETS
merged_df = pd.merge(df_students, df_scores, on="student_id", how="inner")

#CALCULATE EACH STUDENT'S AVERAGE SCORE
merged_df["average_score"] = merged_df[["python","math", "database"]].mean(axis=1)

#FIND THE TOP 5 STUDENTS
top_5_students = merged_df["average_score"].sort_values(ascending=False).head(5)
print(top_5_students[["name", "average_score"]])

#COMPUTE THE AVERAGE SCORE FOR EACH MAJOR
average_score_by_major = merged_df["average_score"].groupby(merged_df["major"])["average_score"].mean()    