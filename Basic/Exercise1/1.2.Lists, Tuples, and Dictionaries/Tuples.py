# We've just been using lists, which allow you to append new members to the list. Sometimes if you know you're
# not going to want to change anything in a list you may want to use an immutable collection called a tuple. It
# othewise works the same as as list but to create one you use parentheses instead of brackets. You can also
# create them with commas, so the following tuples are identical:
mytuple1 = 5, 7, "name", 8
mytuple2 = (5, 7, "name", 8)
print(mytuple1)
print(mytuple2)

# So we might use tuples in the above example. While we may want to append to the set of addresses, each
# individual address could be a tuple. So create a comparable example this way:

address1 = (1212, "First St", "SF", "CA")
address2 = (2323, "Second St", "Seattle", "WA")
address3 = (3434, "Third St", "Denver", "CO")
Addresses = []
Addresses.append(address1)
Addresses.append(address2)
Addresses.append(address3)
print(Addresses)
print(Addresses[0])
print(Addresses[1][1])
print(Addresses[2][3])
print(Addresses[2][0])
