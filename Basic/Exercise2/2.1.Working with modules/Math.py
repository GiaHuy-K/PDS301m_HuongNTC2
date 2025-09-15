import math
print(math.log10(100))
print(math.log(100))
print(math.pi) 
pi = math.pi 
print(pi)

sin = math.sin; cos = math.cos; tan = math.tan
print(sin(0))
print(cos(0))
print(sin(pi))
print(cos(pi))

asin = math.asin; acos = math.acos; atan2 = math.atan2
print(sin(math.radians(45)))
print(sin(45/180*pi))
print(math.degrees(asin(0.5)))
print(asin(0.5)/pi*180)

x0 = 14; y0 = 8
x1 = 17; y1 = 12
dx = x1-x0; dy = y1-y0
h = (dx**2 + dy**2)**0.5
print(h)
print(math.hypot(dx,dy))

import matplotlib.pyplot as plt
pyplot = plt
pyplot.plot([14,17,17,14],[8,8,12,8])
pyplot.show()

# import matplotlib
# print(matplotlib.__version__)



