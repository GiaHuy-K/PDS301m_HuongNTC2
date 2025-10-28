import csv
import os
import pandas as pd
print("Current Working Directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day10.28.2025")
# 1. How many rows and columns the dataset has?
print("1. How many rows and columns the dataset has?")

# Read CSV file using pandas
df = pd.read_csv("StudentsPerformance.csv")
print("Dataframe Shape:")
print(df.shape)  
print(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
print("=="*20)
print("\n")

# 2. Display unique values in gender and race/ethnicity
print("2. Display unique values in gender and race/ethnicity?")
print("Unique values in gender column:")
print(df['gender'].unique())
print("Unique values in race/ethnicity column:")
print(df['race/ethnicity'].unique())
print("=="*20)
print("\n")

# 3. Find which column has the highest average value
print("3. Find which column has the highest average value?")
average_scores = {
    'math score': df['math score'].mean(),
    'reading score': df['reading score'].mean(),
    'writing score': df['writing score'].mean()
}
highest_avg_column = max(average_scores, key=average_scores.get)
print(f"Column with the highest average score: {highest_avg_column} with average {average_scores[highest_avg_column]}")
print("=="*20)
print("\n")

# 4. Check for missing values.
print("4. Check for missing values.")
print(df.isnull().sum())
print("=="*20)
print("\n")

# 5. Replace any missing test scores with the mean.

print("5. Replace any missing test scores with the mean.")
for column in ['math score', 'reading score', 'writing score']:
    mean_value = df[column].mean()
    df[column] = df[column].fillna(mean_value)
# for column in ['math', 'reading', 'writing']: 
#     mean_value = df[column].mean() 
#     df[column].fillna(mean_value, inplace=True)
print("Missing values after replacement:")
print(df.isnull().sum())
print("=="*20)
print("\n")

# 6. Rename columns to simpler names (e.g., math instead of math score)
print("6. Rename columns to simpler names (e.g., math instead of math score).")
df.rename(columns={
    'math score': 'math',
    'reading score': 'reading',
    'writing score': 'writing'
}, inplace=True)

print("Renamed columns:")
print(df.columns)
print("=="*20)
print("\n")

# 7. Find average scores grouped by gender.
print("7. Find average scores grouped by gender.")
average_by_gender = df.groupby('gender')[['math', 'reading', 'writing']].mean()
print(average_by_gender)
print("=="*20)
print("\n")

# 8. Find which race/ethnicity group performs best in reading.
print("8. Find which race/ethnicity group performs best in reading.")
best_race_group = df.groupby('race/ethnicity')['reading'].mean().idxmax()
print(f"Race/Ethnicity group with highest reading score: {best_race_group}")
print("=="*20)
print("\n")

# 9. Find the student(s) with the highest total score
print("9. Find the student(s) with the highest total score.")
df['total_score'] = df['math'] + df['reading'] + df['writing']
max_total_score = df['total_score'].max()
top_students = df[df['total_score'] == max_total_score]
print("Student(s) with the highest total score:")
print(top_students)
print("=="*20)
print("\n")

# 10. Add a column for total and average scores.
print("10. Add a column for total and average scores.")
print(df[['total_score']])
df['average_score'] = df['total_score'] / 3
print(df[['average_score']])
print("=="*20)
print("\n")

# 11. Create a new column pass_math (True if math ≥ 50).
print("11. Create a new column pass_math (True if math ≥ 50).")
df['pass_math'] = df['math'] >= 50
print(df[['pass_math']])
print("=="*20)
print("\n")

# 12. Show how many students passed all three subjects
print("12. Show how many students passed all three subjects.")
# Điều kiện là: pass_math == True VÀ reading >= 50 VÀ writing >= 50
conditions = (df['pass_math'] == True) & (df['reading'] >= 50) & (df['writing'] >= 50)

passed_all_count = conditions.sum() 
print(f"Number of students who passed ALL THREE subjects: {passed_all_count}")

print("=="*20)
print("\n")

#13 . Save the modified dataset to a new CSV file.
print("13. Save the modified dataset to a new CSV file.")
df.to_csv("StudentsPerformance_Modified.csv", index=False)
print("Modified dataset saved as 'StudentsPerformance_Modified.csv'.")
print("=="*20)
print("\n")