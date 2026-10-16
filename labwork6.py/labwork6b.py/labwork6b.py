import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent

df_scores = pd.read_csv(current_dir / "scores.csv")

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

plt.hist(df_scores["math"], bins=10, alpha=0.5, label="Math Scores", color="blue")
plt.hist(df_scores["python"], bins=10, alpha=0.5, label="Python Scores", color="red")
plt.hist(df_scores["database"], bins=10, alpha=0.5, label="Database Scores", color="green")
plt.title("Distribution of Student Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend()
plt.savefig(current_dir / "histogram.png")
plt.show()
plt.close()