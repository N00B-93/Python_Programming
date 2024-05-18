from random import uniform


class Resistor:
    """
    A class representing a Resistor.

    Attributes:
        nominalValue (float): The Resistor's nominal value.

        tolerance (float): The Resistor's tolerance value.

        actualValue (float): The actual value of the resistor.
    """
    def __init__(self, nominalValue=0.0, tolerance=0.0):
        self.nominalValue = nominalValue
        self.tolerance = tolerance
        self.actualValue = self.calculateActualResistance()

    def calculateActualResistance(self):
        """
        Calculates the actual value of a Resistor.

        Returns: None.
        """
        minResistance = self.nominalValue - (self.nominalValue * self.tolerance / 100)
        maxResistance = self.nominalValue + (self.nominalValue * self.tolerance / 100)
        return round(uniform(minResistance, maxResistance), 2)

    def getNominalValue(self):
        """
        Method that returns the Nominal value of a Resistor.

        Returns: (float) The Nominal value of a Resistor.
        """
        return self.nominalValue

    def getTolerance(self):
        """
        Method that returns the Tolerance value of a Resistor.

        Returns: (float) The Resistor's Tolerance value.
        """
        return self.tolerance

    def getActualValue(self):
        """
        Methods that returns the Actual value of a Resistor.

        Returns: (float) The Actual value of a Resistor.
        """
        return self.actualValue


def main() -> None:
    # Demonstrating the Resistor class for ten 330 Ω ± 10 percent resistors
    for _ in range(10):
        resistor = Resistor(330, 10)
        print("\nNominal Resistance:", resistor.getNominalValue(), "Ω")
        print("Tolerance:", resistor.getTolerance(), "%")
        print("Actual Resistance:", resistor.getActualValue(), "Ω")
        print()


if __name__ == "__main__":
    main()
