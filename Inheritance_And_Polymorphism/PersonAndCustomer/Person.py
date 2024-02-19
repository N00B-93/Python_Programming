class Person(object):
    """
    A class that represents a Person.

    Attributes:
        name (str): The name of the person.

        address (str): The address of the person.

        telephoneNumber (str): The telephone number of the person.
    """
    def __init__(self, name, address, telephoneNumber):
        self.__name = name
        self.__address = address
        self.__telephoneNumber = telephoneNumber

    def getName(self):
        """
        Returns the name of the person.

        :return: (str) The name of the person.
        """
        return self.__name

    def getAddress(self):
        """
        Returns the address of the person.

        :return: (str) The address of the person.
        """
        return self.__address

    def getTelephoneNumber(self):
        """
        Returns the telephone number of the person.

        :return: (str) The telephone number of the person.
        """
        return self.__telephoneNumber

    def setName(self, name):
        """
        Sets the name of the person to the given name.

        :param name: (str) The name of the person.

        :return: (None).
        """
        self.__name = name

    def setAddress(self, address):
        """
        Sets the address of the person to the given address.

        :param address: (str) The address of the person.

        :return: (None).
        """
        self.__address = address

    def setTelephoneNumber(self, telephoneNumber):
        """
        Sets the telephone number of the person to the given telephoneNumber.

        :param telephoneNumber: (str) The telephone number of the person.

        :return: (None).
        """
        self.__telephoneNumber = telephoneNumber
