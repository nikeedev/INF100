from math import cos, sin, asin, sqrt, radians

print("Coordinate 1")
long1 = radians(float(input("longitude = ")))
lat1 = radians(float(input("latitude = ")))

print("\nCoordinate 2")
long2 = radians(float(input("longitude = ")))
lat2 = radians(float(input("latitude = ")))

R = 6371000 # metre
 
distance = 2 * R * asin(sqrt(((sin((lat2-lat1) / 2))**2) + cos(lat1)*cos(lat2)*((sin((long2-long1)/2)))**2))

print(f"The distance (m) is {distance}")
