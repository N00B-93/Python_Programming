class Employee:
    """
    A class representing an Employee

    Attributes:
        employeeName: (str) the name of the Employee.

        employeeID (int) The ID number of the Employee.

        department (str) The department of the Employee.

        jobTitle (str) The Employee's job title.
    """
    def __init__(self, employeeName, employeeID, department, jobTitle):
        self.__employeeName = employeeName
        self.__employeeID = employeeID
        self.__department = department
        self.__jobTitle = jobTitle

    def getEmployeeName(self):
        """
        Returns the Employee's Name.

        :return: (str) The Employee's Name.
        """
        return self.__employeeName

    def getEmployeeID(self):
        """
        Returns the Employee's ID number.

        :return: (int) The Employee's ID number.
        """
        return self.__employeeID

    def getDepartment(self):
        """
        Returns the department of the Employee.

        :return: (str) The department of the Employee .
        """
        return self.__department

    def getJobTitle(self):
        """
        Returns the jobTitle of the Employee.

        :return: (str) The job Title of the employee.
        """
        return self.__jobTitle

    def setDepartment(self, department):
        """
        Sets the department of the Employee to the given value.

        :param department: (str) The department of the Employee.

        :return: None.
        """
        self.__department = department

    def setJobTitle(self, jobTitle):
        """
        Sets the jobTitle of the Employee to the given value.

        :param jobTitle: (str) The jobTitle of the Employee.

        :return: None.
        """
        self.__jobTitle = jobTitle

    def setEmployeeID(self, employeeID):
        """
        Sets the ID of the Employee to the given value.

        :param employeeID: (int) The ID of the Employee.

        :return: None.
        """
        self.__employeeID = employeeID

    def setEmployeeName(self, employeeName):
        """
        Sets the name of the Employee to the given value.

        :param employeeName: (str) The name of the Employee.

        :return: None.
        """
        self.__employeeName = employeeName
