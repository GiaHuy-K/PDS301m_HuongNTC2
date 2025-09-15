import math
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
def distangle(pt0, pt1):
    dx = pt1[0] - pt0[0]
    dy = pt1[1] - pt0[1]
    # khoảng cách
    dist = math.sqrt(dx**2 + dy**2)
    # góc (tính theo độ, từ trục X)
    angle = math.degrees(math.atan2(dx, dy))
    return (dist, angle)
origin = (0,0)
for pt in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
    dist, angle = distangle(origin,pt)
    x = np.array([origin[0],pt[0]])
    y = np.array([origin[1],pt[1]])
    print(plt.plot(x,y))
    print(plt.text(*pt, str(angle % 360), size=18)) 
plt.show()


a = (520382, 4152373)
b = (520782, 4152673)
def dist(x1,y1,x2,y2):
    import math
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)
print(dist(*a, *b))