# 7.	Create a dictionary from a given list (zip function)

keys = ["name", "age", "city"]
values = ["Huy", 20, "HCM"]

# tạo dictionary bằng zip
d = dict(zip(keys, values))

print(d)

# 8.	Create a list from the dictionary
d = {"a": 1, "b": 2, "c": 3}

# Lấy list keys
list_keys = list(d.keys())      
print(list_keys)   # ['a', 'b', 'c']

# Lấy list values
list_values = list(d.values())  
print(list_values) # [1, 2, 3]

# Lấy list (key, value)
list_items = list(d.items())    
print(list_items)  # [('a', 1), ('b', 2), ('c', 3)]

# 9.	Create a list of tuples from the dictionary
d = {"a": 1, "b": 2, "c": 3}

# tạo list tuple (key, value)
list_of_tuples = list(d.items())

print(list_of_tuples)

# 10.	How can you delete key-value pair from Dictionary?
# Cách 1. Dùng del : Xóa theo key, nếu key không tồn tại thì báo lỗi.

d = {"a": 1, "b": 2, "c": 3}
del d["b"]
print(d)  # {"a": 1, "c": 3}

# 2. Dùng pop(key[, default]) : Xóa và trả về value. Nếu có default thì không lỗi khi key không tồn tại.

d = {"a": 1, "b": 2, "c": 3}
val = d.pop("b")
print(val)  # 2
print(d)    # {"a": 1, "c": 3}
# 3. Dùng popitem() : Xóa và trả về cặp (key, value) cuối cùng.

d = {"a": 1, "b": 2, "c": 3}
item = d.popitem()
print(item)  # ("c", 3)
print(d)     # {"a": 1, "b": 2}

# 11.	Is the dictionary mutable?
# Dictionary là mutable 
# Nghĩa là sau khi tạo, ta có thể thêm, sửa, hoặc xóa phần tử trong nó.
# Trái ngược với immutable (như tuple, string) thì dictionary có thể thay đổi nội dung mà không cần tạo mới.
# Tạo dictionary ban đầu
d = {"a": 1, "b": 2}
print("Ban đầu:", d)

# Thêm phần tử
d["c"] = 3
print("Sau khi thêm:", d)

# Sửa giá trị
d["a"] = 100
print("Sau khi sửa:", d)

# Xóa phần tử
del d["b"]
print("Sau khi xóa:", d)

# 12.	Given two lists, create a dictionary from them.
# like 7.
# 13.	Write a code to sort dictionaries using a key.
d = {"c": 3, "a": 1, "b": 2}

# sắp xếp theo key
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)
# sắp xếp ngược lại 
sorted_dict_desc = dict(sorted(d.items(), reverse=True))
print(sorted_dict_desc)
# {'c': 3, 'b': 2, 'a': 1}
