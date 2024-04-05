import math
from Functions.TemperatureConverter import fahrenheitToCelsius

"""
    This is a program that models a thermistor alarm used to monitor the temperature of crops in a farm. 
    Thermistors are semiconductor devices that exhibit a temperature dependent resistance described by the equation;
                        R = Roeβ((1/T) - (1/To))
                where R is the resistance, in Ω, at the temperature T, in °K, and R0 is the resistance, 
                in Ω, at the temperature T0, in °K. β is a constant that depends on the material used to 
                make the thermistor.
                
    The alarm with the aid of the thermistor sounds a buzzer if the temperature drops below freezing point. The circuit 
    is designed so that the buzzer goes off when;
                        R2 / (R + R2) < R4 / (R3 + R4)
                        
    The thermistor used in the alarm circuit has R0 = 33,192 Ω at T0 = 40 °C, and β = 3,310 °K. (Notice that β has units
    of °K. The temperature in °K is obtained by adding 273° to the temperature in °C.) The resistors R2, R3, and R4 
    have a resistance of 156.3 kΩ = 156,300 Ω.
    
    This program prompts the user for a temperature in °F and prints a message indicating whether or not the alarm will 
    sound at that temperature.
"""


# Initializes the given circuit parameters.
Ro = 33_192
To = 40 + 273  # Converts 40 °C to °K
β = 3_310
R2 = R3 = R4 = 156.3e3

# Reads in the temperature in Fahrenheit.
T = float(input("\nEnter the temperature in °F: "))

# Converts the temperature from Fahrenheit to Celsius.
TInCelsius = fahrenheitToCelsius(T)

# Calculates the resistance, R.
R = Ro * math.exp(β * (1 / (TInCelsius + 273) - (1 / To)))

# Determines whether the buzzer rings or not.
buzzerRings = (R2 / (R + R2)) < (R4 / (R3 + R4))

# Displays whether the buzzer will ring or not at the temperature entered by the user.
if buzzerRings:
    print(f"\nThe Buzzer will ring at {TInCelsius} °C.")
else:
    print(f"\nThe Buzzer won't ring at {TInCelsius} °C.")
