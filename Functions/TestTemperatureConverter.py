from TemperatureConverter import celsiusToFahrenheit, fahrenheitToCelsius

"""
    This is a program that uses the TemperatureConversion module to convert temperature
    from Fahrenheit to Celsius and vice versa and then displays the result in a table.
"""


def main():
    celsiusTemperature = 40.0
    fahrenheitTemperature = 120.0

    print("Celsius\t\tFahrenheit\t\t|\t\tFahrenheit\t\tCelsius")
    for counter in range(10):
        print(f"{celsiusTemperature}\t{celsiusToFahrenheit(celsiusTemperature):14.1f}\t\t|\t\t{fahrenheitTemperature}"
              f"\t{fahrenheitToCelsius(fahrenheitTemperature):15.2f}")
        celsiusTemperature -= 1.0
        fahrenheitTemperature -= 10.0


if __name__ == "__main__":
    main()
