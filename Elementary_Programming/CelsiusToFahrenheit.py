"""
    This is a program that prompts the user to enter a temperature
    in Celsius, converts it to Fahrenheit and then displays the result.
"""

# Prompts the user to enter Celsius temperature.
celsius = eval(input("\nEnter Celsius Temperature: "))

# Calculate the Fahrenheit equivalent.
fahrenheit = 9 / 5 * celsius + 32

# Displays the result.
print(f"\n{celsius} Celsius is {fahrenheit} Fahrenheit")
