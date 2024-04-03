from math import log, e

"""
    This is a program that prompts the user to enter the relative humidity RH and temperature T in degrees and
    displays the dew point temperature using the formula:
            Td = b * f(T, RH) / (a - f(T, RH)), where
            f(T, RH) = (a * T / b + T)In(RH), where a = 17.2 and b = 237.7° C.
"""


a, b = 17.2, 237.7

# Reads in the relative humidity, RH.
relativeHumidity = float(input("\nEnter a relative humidity in the range 0.0 <= RH <= 1.0: "))

# Reads in the temperature in ° C.
temperature = float(input("\nEnter the temperature in ° C: "))

# Determines the value of f(T, RH)
f = (a * temperature / (b + temperature)) + log(relativeHumidity, e)

# Determines the dew point temperature.
dewPointTemperature = b * f / (a - f)

# Displays the result.
print(f"\nThe dew point temperature is: {dewPointTemperature:.2f}° C")
