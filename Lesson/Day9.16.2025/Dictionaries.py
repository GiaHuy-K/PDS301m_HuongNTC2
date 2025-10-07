
Student_dict = {
    "s1" : "John", 
    "s2" : "Doe", 
    "s3" : "Smith", 
    "s4" : "Alice"
}
print(Student_dict)
print(len(Student_dict))
print(type(Student_dict))
print(Student_dict.keys())
print(Student_dict.values())
update_dict = {
    # "name" : "Jane", 
    "s5" : "Bob"
}
print(Student_dict.update(update_dict))
print(Student_dict)
# dictionary lồng nhau
Infor_dict = {
    "s1" : {
    "name" : "John",
    "age" : 21,
    "gender" : "Male",
    "major" : "Computer Science"}
    ,
    "s2" : {
    "name" : "Doe",
    "age" : 22,
    "gender" : "Female",
    "major" : "Mathematics"
    },
    "s3" : {
    "name" : "Smith",
    "age" : 20,
    "gender" : "Male",
    "major" : "Physics"
    },
    "s4" : {
    "name" : "Alice",
    "age" : 23,
    "gender" : "Female",
    "major" : "Biology"
    },
    "s5" : {
    "name" : "Bob",
    "age" : 21,
    "gender" : "Male",
    "major" : "Mathematics"
    }
}
Student_dict.update(Infor_dict)
print("\nUpdated Student Dictionary:")
print(Student_dict)

#dictionary lấy từ hai list
keys = ["Acer", "Asus", "Dell", "HP"]
values = [500, 600, 700, 800]
laptop_dict = dict(zip(keys, values))

print("\nLaptop Dictionary:")
print(laptop_dict)
laptop_dict["B Laptop"] = 900
print("\nUpdated Laptop Dictionary:")
print(laptop_dict)

# sort dictionary by keys
sorted_laptop_dict = dict(sorted(laptop_dict.items()))
print("\nSorted Laptop Dictionary by Keys:")
print(sorted_laptop_dict)

import operator
# sort dictionary by values
# dic_sort = dict(sorted(laptop_dict.items(), key=operator.itemgetter(1)))
# print(dic_sort)

# nối 3 cái dict lại thành 1 
# cách 1 dùng | (python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
merged_dict1 = dict1 | dict2 | dict3
print("\nMerged Dictionary using | operator:")
print(merged_dict1)
# cách 2 unpacking (python 3.5+)
merged_dict = {**dict1, **dict2, **dict3}
print("\nMerged Dictionary:")   
print(merged_dict)

# cách 3 dùng update (python nào cũng rứa thâu)
dict4 ={}
for d in (dict1, dict2, dict3):
    dict4.update(d)
print("\nMerged Dictionary using update():")
print(dict4)



# Xóa phần tử trong dictionary
# cách 1 xóa hết những phần tử có key 
print("\nMerged dict4:")
print(dict4)
i = dict4.keys()
if "d" in i:
    del dict4["d"]
    
print("\nMerged dict4 after removing :")
print(dict4)

# cách 2 xóa đúng 1 phần tử có key đó
for i in list(dict4.keys()):
    if i == "d":      # 🔹 chỉ xóa khi key đúng bằng "d"
        del dict4["d"]
print("\nMerged dict4 after removing :")
print(dict4)