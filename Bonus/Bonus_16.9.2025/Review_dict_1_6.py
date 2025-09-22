# 1.	What is a dictionary?
# -Trong Python, từ điển (Dictionary) là một kiểu dữ liệu Dict tích hợp sẵn được dùng để lưu trữ dữ liệu dưới dạng các cặp key – value. 
# -Đây là một tập hợp không có thứ tự, có thể thay đổi và được lập chỉ mục. 
# -Mỗi khóa trong từ điển là duy nhất và ánh xạ đến một giá trị. 
# -dictionaries thường được dùng để lưu trữ dữ liệu có liên quan, chẳng hạn như thông tin về một đối tượng hoặc thực thể, 
# giúp truy xuất dữ liệu nhanh hơn thông qua key.
# -Key phải duy nhất, value có thể trùng.
dictionary1 = { "name": "huy", "major" : "DA"}

# 2.	Are dictionaries case-sensitive?
# Có. Key "Name" và "name" được coi là khác nhau.
dictionary2 = { "name": "huy", "Name" : "HẢ"}
print("name: ",dictionary2["name"])
print("Name: ",dictionary2["Name"])

# 3.	What are different ways of creating a Dictionary? ( 4 ways, try it yourself)

d1= {"huy": " hả"} # Cách 1. Dùng dấu ngoặc nhọn {} trực tiếp

d2 = dict(a=1, b=2) # Cách 2. Dùng hàm dict() với tham số keyword

d3 = dict([("a", 1), ("b", 2)]) # Cách 3. Dùng dict() với list/tuple cặp (key, value)

# Cách 4. Dùng zip() để ghép 2 list lại:
keys = ["a", "b"]
values = [1, 2]
d4 = dict(zip(keys, values))

# 4.	What is a Nested Dictionary? How is it created?
# Nested Dictionary Là dictionary chứa dictionary khác.
nested = {
    "student1": {"name": "Anh", "age": 20},
    "student2": {"name": "Bình", "age": 21}
}
print(nested)
# 5.	How do you add an element in Dictionary? (3 ways, try it yourself)
d = {"a": 1}

# Cách 1: gán trực tiếp
d["b"] = 2

# Cách 2: dùng update()
d.update({"c": 3})

# Cách 3: dùng setdefault()
d.setdefault("d", 4)
print(d)
# 6.	Methods in dictionary: clear(), copy(), items(), keys(), values(), update(), ...

# 1. clear() : Xóa hết phần tử trong dict.
d = {"a": 1, "b": 2}
d.clear()
print(d)  # {}

# 2. copy() : sao chép dictionary.
d = {"a": 1, "b": 2}
d2 = d.copy()
print(d2)  # {"a": 1, "b": 2}

# 3. fromkeys(seq, value=None) : Tạo dict mới với key từ seq, value mặc định.
d = dict.fromkeys(["a", "b", "c"], 0)
print(d)  # {"a": 0, "b": 0, "c": 0}

# 4. get(key, default=None) : Lấy value theo key, nếu không có thì trả về default.
d = {"a": 1}
print(d.get("a"))      # 1
print(d.get("b", -1))  # -1

# 5. items() : Trả về view object dạng (key, value).
d = {"a": 1, "b": 2}
print(list(d.items()))  # [("a", 1), ("b", 2)]

# 6. keys() : Trả về view object chỉ chứa key.
d = {"a": 1, "b": 2}
print(list(d.keys()))  # ["a", "b"]

# 7. values() : Trả về view object chỉ chứa value.
d = {"a": 1, "b": 2}
print(list(d.values()))  # [1, 2]

# 8. pop(key, default) : Xóa key và trả về value. Nếu không có key thì trả về default.
d = {"a": 1, "b": 2}
print(d.pop("a"))  # 1
print(d)           # {"b": 2}

# 9. popitem() : Xóa và trả về cặp (key, value) cuối cùng.
d = {"a": 1, "b": 2}
print(d.popitem())  # ("b", 2)
print(d)            # {"a": 1}

# 10. setdefault(key, default=None) : Nếu key có rồi thì trả về value, nếu chưa thì thêm vào với giá trị default.
d = {"a": 1}
print(d.setdefault("a", 5))  # 1 (đã tồn tại)
print(d.setdefault("b", 5))  # 5 (mới thêm)
print(d)  # {"a": 1, "b": 5}

# 11. update({...}) :Thêm/cập nhật các cặp key–value từ dict khác hoặc iterable.
d = {"a": 1}
d.update({"b": 2, "c": 3})
print(d)  # {"a": 1, "b": 2, "c": 3}
