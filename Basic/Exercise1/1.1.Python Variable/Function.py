# We'll be using a lot of functions, methods and properties, so we should know what they are.
# Functions are written as functionName(input) . We'll see a lot of these in the math module, but you can
# see what the built-in functions are at https://docs.python.org/3/library/functions.html
# (https://docs.python.org/3/library/functions.html)

import math
sin = math.sin
radians = math.radians
pi = math.pi
print(abs(-5)   )  # absolute value function, returns 5
print(sin(30/180 * pi) ) # sin(30 degrees) = 0.5
print(sin(radians(30)))  # sin(30 degrees) = 0.5

# Methods are written as obj.method(parameters) and applies to that object. To see what methods apply
# to an object, type the dot and press tab. There aren't many for the simple numeric variables. Try it out, but
# here's one example.
# y = 0.5
# y.
# y.as_integer_ratio() / biến thành phân số

y = 0.5
print(y.as_integer_ratio())  # (1, 2)

mystr = "hello"
print(mystr.capitalize())  # Hello

# Properties are similar to methods in being applied to an object, but there are no parameters, thus no () ;
# they simply are a property of some sort. Once again, to see what properties are available to an object, press
# tab after the dot. Try it out
# x = 2
# x.
# x.denominator
x = 2
print(x.denominator)
