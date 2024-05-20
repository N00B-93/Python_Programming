from Country import Country
from copy import deepcopy

"""
    This is a program that creates five Country Objects, adds them to a list and then displays the Country with the
    greatest land area, largest population and largest population density.
"""


def getCountryWithLargestPopulation(countries: list[Country]) -> Country:
    """
    This determines the Country with the largest population from a list of Countries.

    Args:
        countries: (list) A list of Countries.

    Returns:
        The Country with the largest population.
    """
    countryWithMaxPopulation: Country = deepcopy(countries[0])

    for country in countries:
        if country.population > countryWithMaxPopulation.population:
            countryWithMaxPopulation = deepcopy(country)
    return countryWithMaxPopulation


def getCountryWithLargestLandArea(countries: list[Country]) -> Country:
    """
    This determines the Country with the largest land area from a list of Countries.

    Args:
        countries: (list) A list of Countries.

    Returns:
        The Country with the largest land area.
    """
    countryWithLargestLandArea: Country = deepcopy(countries[0])

    for country in countries:
        if country.area > countryWithLargestLandArea.area: 
            countryWithLargestLandArea = deepcopy(country)
    return countryWithLargestLandArea


def getCountryWithLargestPopulationDensity(countries: list[Country]) -> Country:
    """
    This determines the Country with the largest population density.
    
    Args:
        countries: (list) A list of Countries.

    Returns:
        The Country with the largest population density.
    """
    countryWithLargestPopulationDensity: Country = deepcopy(countries[0])

    for country in countries:
        if (country.population / country.area) > (countryWithLargestPopulationDensity.population /
                                                  countryWithLargestPopulationDensity.area):
            countryWithLargestPopulationDensity = deepcopy(country)
    return countryWithLargestPopulationDensity


def main() -> None:
    # Empty list to hold the countries created.
    countries: list = []

    # Creates 5 Country Objects.
    country1 = Country("Nigeria", 254_789_563, 2_106_559.24)
    country2 = Country("China", 2_145_565_996, 4_126_578.78)
    country3 = Country("India", 1_545_765_996, 3_227_785.11)
    country4 = Country("U.S.A", 365_212_448, 2_714_570.25)
    country5 = Country("Russia", 145_565_996, 6_727_884.76)

    # Adds the countries to the list
    countries.append(country1)
    countries.append(country2)
    countries.append(country3)
    countries.append(country4)
    countries.append(country5)
    
    # Displays the countries with the highest population, highest land area and highest population density.
    print(f"\nThe country with the Largest Population is: {getCountryWithLargestPopulation(countries).countryName}")
    print(f"\nThe country with the Largest Land Area is: {getCountryWithLargestLandArea(countries).countryName}")
    print(f"\nThe country with the Highest Population density is: "
          f"{getCountryWithLargestPopulationDensity(countries).countryName}")

    # Displays information about each Country.
    [print(country.__str__()) for country in countries]


if __name__ == "__main__":
    main()
