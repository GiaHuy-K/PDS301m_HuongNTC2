# Another data type is Boolean, meaning True or False . The constants that can be used to assigns these are
# literally True and False , but these are typically created by evaluating an expression, like 5 > 6
tf = 5 > 6
print(tf)
print(type(tf))
print(type(True))

# It's often useful to realize that True can also be interpreted or entered as the integer 1 , and False is 0 as
# you can see by including the Boolean variable in a mathematical expression like False * 2 or True * 2 .

print(False * 2)
print(True * 2)

#In fact, any non-zero value will be interpreted as True , but False is always zero.
print(bool(3))
print(bool(0))
print(bool(-5))
print(bool(0.0))
print(bool(0.0001))
print(bool(-0.0001))