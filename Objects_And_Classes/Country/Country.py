class Country:
    """
    A class representing a Country.

    Attributes:
        countryName (str): The name of the Country.

        population (int): The number of people in the Country.

        area (float): The land area of the Country in sqKm.
    """
    def __init__(self, countryName, population, area):
        self.countryName = countryName
        self.population = population
        self.area = area
    
    def __str__(self):
        """
        This describes a Country.

        :return: (str) A String describing a Country.
        """
        return (f"\nCountry Name: " + self.countryName + "\nPopulation: " + f"{self.population}" + "\nLand Area: " +
                f"{self.area}" + "sqKm")
