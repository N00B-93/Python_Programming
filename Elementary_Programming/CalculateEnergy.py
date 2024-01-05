"""
    This is a program that calculates the energy needed to
    heat water from an initial temperature to a final temperature.
"""

# Reads in the amount of water.
waterAmount = float(input("\nEnter the amount of water in kg: "))

# Reads in the initial Temperature.
initialTemperature = float(input("Enter the initial temperature: "))

# Reads in the final temperature.
finalTemperature = float(input("Enter the final temperature: "))

# Calculates the total energy.
totalEnergy = waterAmount * (finalTemperature - initialTemperature) * 4184

# Displays the result.
print(f"\nThe energy needed is: {totalEnergy}")
