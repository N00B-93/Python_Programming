from Employee import Employee


class ProductionWorker(Employee):
    """
        A class Representing a Production Worker that inherits from Employee class.

        Attributes:
              shift (int): The shift of the employee.

              hourlyPayRate (float): The hourly payment rate of the employee.
    """
    def __init__(self, shift, hourlyPayRate, name, ID):
        super().__init__(name, ID)
        self.__shift = shift
        self.__hourlyPayRate = hourlyPayRate

    def getShift(self):
        """
        Returns the shift of the employee.

        :return: (int) The shift of the employee.
        """
        return self.__shift

    def getHourlyPayRate(self):
        """
        Returns the hourly payment rate of the employee.

        :return: (float) The hourly payment rate of the employee.
        """
        return self.__hourlyPayRate

    def setShift(self, shift):
        """
        Sets the shift of the employee to the given shift.

        :param shift: (int) The shift of the employee.

        :return: (None)
        """
        self.__shift = shift

    def setHourlyPayRate(self, hourlyPayRate):
        """
        Sets the hourly payment rate of the employee.

        :param hourlyPayRate: (float) The hourly payment rate of the employee.

        :return: (None).
        """
        self.__hourlyPayRate = hourlyPayRate

    def __str__(self):
        """
        Returns the String representation of the Production Worker Object.

        :return: (str) The string representation of the Production Worker Object.
        """
        if self.getShift() == 1:
            return (super().__str__() + "\nShift: " + 'Day' + "\nHourly Pay: $ " +
                    str(self.__hourlyPayRate))
        return (super().__str__() + "\nShift: " + 'Night' + "\nHourly Pay: $ " +
                str(self.__hourlyPayRate))
