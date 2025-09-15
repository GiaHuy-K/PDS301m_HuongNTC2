import math

lat = 37
decls = [-23.44, -20, -12, 0, 12, 20, 23.44, 20, 12, 0, -12, -20]

sunangles = []
azimuths = []

for d in decls:
    # Góc cao mặt trời (altitude)
    sun_angle = 90 - abs(lat - d)
    sunangles.append(sun_angle)
    
    # Góc phương vị (azimuth), ví dụ giả định trưa (mặt trời ở hướng Nam nếu ở Bắc bán cầu)
    azimuth = 180 if lat > 0 else 0
    azimuths.append(azimuth)

print("decls:", decls)
print("sunangles:", sunangles)
print("azimuths:", azimuths)
