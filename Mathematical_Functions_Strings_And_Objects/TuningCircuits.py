from math import sqrt, pi

"""
    This is a program that prompts the user to enter a frequency f, maximum capacitance Cmax, and minimum capacitance 
    Cmin and the displays the inductance L, and the frequency range to which the circuit can be tuned by varying the 
    capacitance.
    The formula for the Inductance, fmin and fmax are;
            L = (2π / f) ^ 2 / C, where C = √Cmin * √Cmax 
            fmin = 2π / √LCmin and fmax = 2π / √LCmax
"""

# Reads in the frequency.
frequency = float(input("\nEnter the frequency: "))

# Reads in the minimum capacitance.
minCapacitance = float(input("\nEnter the minimum capacitance: "))

# Reads in the maximum capacitance.
maxCapacitance = float(input("\nEnter the maximum capacitance: "))

# Calculates the effective capacitance.
effectiveCapacitance = sqrt(minCapacitance * maxCapacitance)

# Calculates the Inductance of the tuning circuit.
inductance = pow(2 * pi / frequency, 2) / effectiveCapacitance

# Calculates the minimum frequency.
minFrequency = (2 * pi) / sqrt(inductance * minCapacitance)

# Calculates the maximum frequency.
maxFrequency = (2 * pi) / sqrt(inductance * maxCapacitance)

# Displays the Inductance.
print(f"\nThe Inductance of the tuning circuit is: {inductance:.2f} H")

# Displays the frequency range of the tuning circuit.
print(f"\nThe range of frequencies to which the circuit can be tuned is {minFrequency:.2e} <= f <= {maxFrequency:.2e}")
