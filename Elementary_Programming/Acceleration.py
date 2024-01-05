"""
    This is a program that prompts the user to enter the starting velocity v0 in
    meters/second, the ending velocity v1 in meters/second, and the time span t in
    seconds, and displays the average acceleration.
"""

# Reads in the initial velocity.
initialVelocity = float(input("\nEnter the initial velocity in meters/second: "))

# Reads in the final velocity.
finalVelocity = float(input("\nEnter the final velocity in meters/second: "))

# Reads in the time.
time = float(input("\nEnter the time in seconds: "))

# Calculates the acceleration.
acceleration = (finalVelocity - initialVelocity) / time

# Displays the result.
print(f"The average acceleration is: {acceleration:.2f}")
