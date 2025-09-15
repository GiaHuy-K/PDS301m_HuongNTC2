def distance(pt0, pt1):
    import math
    dx = pt1[0] - pt0[0]
    dy = pt1[1] - pt0[1]
    return math.sqrt(dx**2 + dy**2)
a = (520382, 4152373)
b = (520782, 4152673)
print(distance(a, b))

c = [520382, 4152373]   # list (x, y)
d = [520782, 4152673]   # list (x, y)

print(distance(c, d))
#typle and list 
e = (520382, 4152373) # dict {'x': x, 'y': y}
f = [520782, 4152673]  # dict {'x': x, 'y': y}
print(distance(e, f))

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
x = np.array([a[0],a[0],b[0],a[0]])
y = np.array([a[1],b[1],b[1],a[1]])
fig, ax = plt.subplots()
print(plt.plot(x,y))
ax.axis('equal')
print(plt.text(*a,"a",size=24))
print(plt.text(*b,"b",size=24))
dXlab = (a[0],(b[1]-a[1])/2+a[1])
dYlab = ((b[0]-a[0])/2+a[0],b[1])
print(plt.text(*dXlab,"dX",size=24))
print(plt.text(*dYlab,"dY",size=24))
plt.show()
print(distance(pt1=(520782, 4152673), pt0=(520382, 4152373)))
# bài 2 dùng math.atan2
import math

def distangle(pt0, pt1):
    dx = pt1[0] - pt0[0]
    dy = pt1[1] - pt0[1]
    # khoảng cách
    dist = math.sqrt(dx**2 + dy**2)
    # góc (tính theo độ, từ trục X)
    angle = math.degrees(math.atan2(dx, dy))
    return (dist, angle)


# test
a = (520382, 4152373)
b = (520782, 4152673)

print(distangle(pt0=a, pt1=b))
print(distangle(pt1=b, pt0=a))
print(distangle(pt1=a, pt0=b))


