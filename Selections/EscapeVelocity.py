from math import sqrt

"""
    This is a program that prompts the user to enter a launch velocity and then checks if the velocity is enough to
    escape from the surface of the Halley's Comet.
"""

# Defines the constants used in the program.
UNIVERSAL_GRAVITATIONAL_CONSTANT = 6.67E-11
MASS_OF_HALLEY_COMET = 2.2E14
RADIUS_OF_HALLEY_COMET = 4700

# Calculates the escape velocity on the surface of Halley's Comet.
escapeVelocity = sqrt((2 * UNIVERSAL_GRAVITATIONAL_CONSTANT * MASS_OF_HALLEY_COMET) / RADIUS_OF_HALLEY_COMET)

# Displays the escape velocity on Halley's Comet.
print(f"\nThe escape velocity on Hally's Comet is: {escapeVelocity:.2f}m/s")

# Prompts the user to enter a launch velocity.
launchVelocity = float(input("\nEnter a launch velocity in m/s: "))

# Displays an error message and terminates the program if the user enters a velocity <= 0.
if launchVelocity <= 0:
    print("\nUse a Launch velocity > 0")
    exit(1)

# Checks if the velocity entered by the user is enough to escape from the surface of Halley's Comet or not.
if launchVelocity >= escapeVelocity:
    print(f"\nAn Object launched with the velocity {launchVelocity}m/s will escape from the surface of Halle's Comet.")
else:
    print(f"\nAn Object launched with the velocity {launchVelocity}m/s will not escape from the surface of Halle's "
          f"Comet.")
