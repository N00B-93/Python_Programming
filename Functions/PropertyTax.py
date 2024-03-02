"""
    A county collects property taxes on the assessment value of property, which is 60 percent of 
    the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000.
    The property tax is then 72¢ for each $100 of the assessment value.
    The tax for the acre assessed at $6,000 will be $43.20. This program prompts the user to enter the actual value of a
    piece of property, then displays the
    assessment value and the property tax.
"""


def getAssessmentValue(actualValue):
    """
    Returns the assessment value of a property given the actual value of the property.

    :param actualValue: (float) The property's actual value.

    :return: (float) The property's assessment value.
    """
    return 0.6 * actualValue


def getPropertyTax(assessmentValue):
    """
    Returns the property tax of a property given the property's assessment value.

    :param assessmentValue: (float) The property's assessment value.

    :return: (float) The property tax.
    """
    return assessmentValue / 100 * 0.72


def main() -> None:
    # Prompts the user to enter the property's actualValue.
    actualValue: float = float(input("\nEnter the property's actual value: $ "))

    # Displays the property's assessment value.
    print(f"\nProperty Assessment Value: $ {getAssessmentValue(actualValue):.2f}")

    # Displays the property tax.
    print(f"\nProperty Tax: $ {getPropertyTax(getAssessmentValue(actualValue)):.2f}")


if __name__ == "__main__":
    main()
