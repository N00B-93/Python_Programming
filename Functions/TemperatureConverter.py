"""
    This is a module that contains two functions with headers;
                def celsiusToFahrenheit(celsius):
    and
                def fahrenheitToCelsius(fahrenheit):
    for converting temperature from Celsius to Fahrenheit and vice versa.
"""


def celsiusToFahrenheit(temperature):
    """
    Converts a temperature in Celsius to Fahrenheit.

    :param temperature: (float) The temperature to be converted.

    :return: (float) The Fahrenheit temperature.
    """

    return 9 / 5 * temperature + 32


def fahrenheitToCelsius(temperature):
    """
    Converts a temperature in Fahrenheit to Celsius.

    :param temperature: (float) The temperature to be converted.

    :return: (float) The Celsius temperature.
    """

    return (5 / 9) * temperature - 32
