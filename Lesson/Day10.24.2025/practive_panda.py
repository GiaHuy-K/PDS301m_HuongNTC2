import csv
import pandas as pd
import os

print("Current Working Directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day10.24.2025")
# Read CSV file using pandas
df = pd.read_csv("dataForPandaPractice.csv")

print("First and last 20 rows of the dataframe:")
print(df.head(20))
print(df.tail(20))



#2. Clean above data file and update the CSV file (replace values which contain ?, n.a or NaN
# clean data: xử lý các giá trị thiếu, dữ liệu trùng lặp, định dạng không đúng
# Check for missing values
# print("Missing Values in Each Column:")
# df.replace(['?', 'n.a', 'NaN'], pd.NA, inplace=True)
# print(df.isnull().sum())
df = pd.read_csv("dataForPandaPractice.csv", na_values={
'length':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)
df.to_csv("dataForPandaPractice_Cleaned.csv", index=False)

# tìm xe chiều dài dài nhất
max_length = df['length'].max()
most_expensive_cars = df[df['length'] == max_length]

print(f"Car(s) with the highest length: ", most_expensive_cars)
#4. In ra chi tiet cua cac chiec xe thuoc hang Audi
audi_cars = df[df['company'] == 'audi']
print("Car(s) from Audi: ")
print(audi_cars)