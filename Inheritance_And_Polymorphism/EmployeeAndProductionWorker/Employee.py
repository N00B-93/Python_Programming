class Employee(object):
    """
    A class representing an employee

    Attributes:
        employeeName (str): The name of the employee.

        employeeID (int): The ID of the employee.
    """
    def __init__(self, employeeName, employeeID):
        self.__employeeName = employeeName
        self.__employeeID = employeeID

    def getEmployeeName(self):
        """
        Returns the name of the employee.
        :return: (str) The name of the employee.
        """
        return self.__employeeName

    def getEmployeeID(self):
        """
        Returns the ID of the employee.

        :return: (int) The ID of the employee.
        """
        return self.__employeeID

    def setEmployeeName(self, employeeName):
        """
        Sets the name of the employee with the given name.

        :param employeeName: (str) The name of the employee.

        :return: (None).
        """
        self.__employeeName = employeeName

    def setEmployeeID(self, employeeID):
        """
        Sets the ID of the employee with the given value.

        :param employeeID: (int) The ID of the employee.

        :return: (None).
        """
        self.__employeeID = employeeID

    def __str__(self):
        """
        Returns the string representation of the Employee Object.

        :return: (str) The string representation of the Employee Object.
        """
        return f"\nEmployee Name: {self.__employeeName}\nEmployee ID: {self.__employeeID}"
