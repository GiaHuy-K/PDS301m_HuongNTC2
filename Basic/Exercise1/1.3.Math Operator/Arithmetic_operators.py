print("Addition or subtraction:")
x = 2 + 3
y = 2. + 3
z = 2 - 3
print(type(x), x)
print(type(y), y)
print(type(z), z)

print("Multiply:")
m = 2 * 3
n = 2. * 3
print(type(m), m)
print(type(n), n)

print("Division:")
a = 1 / 2
b = 1. / 2
c = 4 / 2
print(type(a), a)
print(type(b), b)
print(type(c), c)

print("Power:")
d = 2 ** 3
e = 2. ** 3
print(type(d), d)
print(type(e), e)

print("Square root:")
f = 4 ** (1/2)
g = 4. ** 0.5
print(type(f), f)
print(type(g), g)

# Modulus (gives the remainder of a division operation):
print("Modulo:")
print("modulus = 10")
for n in range(2, 14, 2):
    print(n, n % 10) # 10 might be a common repeated value
print("modulus = 360, for compass azimuth (°)")
for n in range(90, 720, 90):
    print(n, n % 360) # Compass azimuth (°) is a good application of modulos in a cycle.

# Conversion functions
# We'll be looking at many additional functions imported from various modules, but there are some functions that
# are so commonly needed that they are built in to the core language. Conversion functions of various types are
# good examples. For example, you often need to convert numbers to other formats, or convert strings to numbers
# and vice-versa.
print("Conversion functions:")
print(str(5.2389))
print(int("4"))

print(float("4.2"))

x = 9.53
y = int(x)
print(y)
z = float(y)
print(z)

#print(int("4.7"))  // Error
x = "7.25"
print(int(float(x)))