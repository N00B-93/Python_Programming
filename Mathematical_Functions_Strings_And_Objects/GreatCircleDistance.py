from math import sin, cos, acos, radians
from typing import Final

"""
    This is a program that prompts the user to enter the latitude and longitude of two
    points on the earth in degrees and displays its great circle distance. The average
    earth radius is 6,371.01 km.
"""

# Constant holding the value of the Earth's radius.
RADIUS_OF_EARTH: Final[float] = 6371.01

# Reads in the Latitude and Longitude for point1 and point2 respectively.
lat1, lon1 = eval(input("\nEnter point 1 (latitude and longitude) in degrees separated by comma: "))
lat2, lon2 = eval(input("\nEnter point 1 (latitude and longitude) in degrees separated by comma: "))

# Converts the latitudes and longitudes from degrees to radians
lat1, lat2 = radians(lat1), radians(lat2)
lon1, lon2 = radians(lon2), radians(lon1)

# Calculates the great circle distance.
greatCircleDistance = RADIUS_OF_EARTH * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))

# Displays the result.
print(f"\nThe distance between two points is {greatCircleDistance:.2f} km")
