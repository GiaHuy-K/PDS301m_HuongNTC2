import pandas as pd
#create dataframe from dictionary
data = {
    "Name": ["Huy","An", "Binh", "Cuong"],
    "Age": [23, 22, 24, 23],
    "City": ["Hanoi", "HCM", "Danang", "Hue"],
    "Grade":[8.5, 9.0, 7.5, 8.0],
    "Hobby": ["Football", "Reading", "Gaming", "Traveling"]
}
#create dataframe with custom index
df = pd.DataFrame(data, index=["SV1", "SV2", "SV3", "SV4"])
print(df)
print("=="*20)
#create dataframe from list of lists
data_list = [
    ["Huy", 23, "Hanoi", 8.5, "Football"],
    ["An", 22, "HCM", 9.0, "Reading"],
    ["Binh", 24, "Danang", 7.5, "Gaming"],
    ["Cuong", 23, "Hue", 8.0, "Traveling"]
]
df2 = pd.DataFrame(data_list, columns=["Name", "Age", "City", "Grade", "Hobby"], index=["SV1", "SV2", "SV3", "SV4"])
print(df2)


import csv
import os

print("Current Working Directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day10.24.2025")
# Read CSV file using pandas
df = pd.read_csv("dataForPandaPractice.csv")
print(df)

#print 5 first rows
print("First 5 rows of the dataframe:")
print(df.head(5))
#print 3 last rows
print("Last 3 rows of the dataframe:")
print(df.tail(3))

# access metadata trong file -->understanding about data detail
print("Dataframe Information:")
print(df.info())

# -->describe() ap dung cac ham thong ke trong toan cho cac cot co kieu du lieu so
print("Statistical Summary:")
print(df.describe())

print("Dataframe Shape:")
print(df.shape)  # prints (number of rows, number of columns)

print("Dataframe Columns:")
print(df.columns)  # prints the column names

print("Dataframe Index:")
print(df.index)  # prints the index (row labels)