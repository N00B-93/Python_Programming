from math import sin, cos, radians

"""
    This is a program that prints the sin and cos 
    of angles from 0 to 360 in steps of 10 degrees.
"""

# Displays the result.
print("\nDegree\t\tSin\t\tCos")
for angle in range(0, 370, 10):
    print(f"{angle}\t\t{sin(radians(angle)):.4f}\t\t{cos(radians(angle)):.4f}")
