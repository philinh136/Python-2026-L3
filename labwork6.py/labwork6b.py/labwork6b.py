import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent

df_scores = pd.read_csv(current_dir / "scores.csv")

#scatter 
plt.scatter(df_scores["student_id"], df_scores["math"], label="Math Scores", color="blue")
plt.scatter(df_scores["student_id"], df_scores["python"], label = "Python Scores", color = "red")
plt.scatter(df_scores["student_id"], df_scores["database"], label = "Database Scores", color = "green")
plt.title("Student Scores in Different Subjects")
plt.xlabel("Student ID")
plt.ylabel("Scores")
plt.legend()
plt.savefig(current_dir / "scattered.png")
plt.show()
plt.close()

#histogram
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

axes[0].hist(df_scores["math"], bins=10, color="blue")
axes[0].set_title("Math Scores")
axes[0].set_xlabel("Scores")
axes[0].set_ylabel("Frequency")

axes[1].hist(df_scores["python"], bins=10, color="red")
axes[1].set_title("Python Scores")
axes[1].set_xlabel("Scores")
axes[1].set_ylabel("Frequency")

axes[2].hist(df_scores["database"], bins=10, color="green")
axes[2].set_title("Database Scores")
axes[2].set_xlabel("Scores")
axes[2].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(current_dir / "histo.png")
plt.show()
plt.close()

#box 
plt.boxplot([df_scores["math"].dropna(), df_scores["python"].dropna(), df_scores["database"].dropna()])
plt.title("Score Distribution by Subject")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.xticks([1, 2, 3], ["Math", "Python", "Database"])
plt.savefig(current_dir / "box.png")
plt.show()
plt.close()