from math import pow

"""
    This program prompts the user to enter a temperature between and
    41°F and a wind speed greater than or equal to 2 and displays the wind-chill temperature.
"""

# Reads in the outside temperature.
temperature = float(input("\nEnter the temperature in Fahrenheit between -58 and 41: "))

# Reads in a wind speed greater than 2 mph.
windSpeed = float(input("\nEnter the wind speed > 2 miles per hour: "))

# Calculates the wind chill index.
windChillIndex = (35.74 + 0.6215 * temperature - 35.75 *
                  pow(windSpeed, 0.16) + 0.4275 * temperature * pow(windSpeed, 0.16))

# Displays the result.
print(f"\nThe wind-chill index is: {windChillIndex:.3f}")
