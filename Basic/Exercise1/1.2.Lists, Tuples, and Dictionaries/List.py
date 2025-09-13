# To make data much more useful than simple scalar variables, programming languages make use of sets of data,
# traditionally called arrays. We'll be looking at a variety of types of these, eventually getting to NumPy arrays and
# pandas.DataFrames, where we'll work with data like a database. We'll start with looking at the most common set
# type, the list, and then immutable lists called tuples and look-up systems called dictionaries. These will all
# serve important purposes in working with data of various types, and especially the spatial data that we're most
# concerned about.

#list
empty_list = []
print(type(empty_list))  # <class 'list'>
aList = [5,7.89,"Fred"]
print(aList)  

x = 5
msg = "Hello"
path = "c:/py/data"
anotherList = [x, msg, path,2.7, aList]
print(anotherList) 


print(a := 2)
b = a + 3
print(b)
wspath = "c:\data\excer"
print(wspath) 
print("\n")
# Subsetting lists:
# You can pull out a subset of a list (sometimes called slicing) by using list indices defining the position or positions
# of list items that you want to extract. This takes a bit of getting used to, but the key is to know that the index
# refers to a position between each element in a list, as shown here.
# lyr = ["geology", "landuse", "publands", "streams", "cities"]
#             0          1        2           3          4    5
lyr = ["geology", "landuse", "publands", "streams", "cities"]
print(lyr[1])  
print(lyr[1:2]) 
print(lyr[0:2])
print(lyr[0:3])
print(lyr[-2:])
print(lyr[-1])
print(lyr[:1])
print("\n")
print(lyr[1:2])
print(lyr[1:2][0])
print(lyr[1]==lyr[1:2][0])
print("\n")

a1 = [1212, "First St", "SF", "CA"]
a2 = [2323, "Second St", "Seattle", "WA"]
a3 = [3434, "Third St", "Denver", "CO"]
Addresses = []
Addresses.append(a1)
Addresses.append(a2)
Addresses.append(a3)
print(Addresses[0])
print(Addresses[1][1])
print(Addresses[2][3])
print(Addresses[2][0])

print("\n")
my_schedule = [
    "Gia Huy",
    [["GEOG", 625], ["MATH", 202], ["CS", 101]]
]

print(my_schedule)

