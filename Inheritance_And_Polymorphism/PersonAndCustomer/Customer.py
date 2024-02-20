from Person import Person


class Customer(Person):
    """
    A class that represents a Customer.

    Attributes:
        customerID (int): The ID of the Customer.

        onMailingList (bool): Whether this Customer is on a Mailing List.
    """

    def __init__(self, customerID, onMailingList, name, address, phoneNumber):
        super().__init__(name, address, phoneNumber)
        self.__customerID = customerID
        self.__onMailingList = onMailingList

    def getCustomerID(self):
        """
        Returns the ID of the Customer.

        :return: (int) The ID of the Customer.
        """
        return self.__customerID

    def setCustomerID(self, customerID):
        """
        Sets the ID of the Customer to the given customer ID.

        :param customerID: (int) The ID of the Customer.

        :return: (None) The ID of the Customer.
        """
        self.__customerID = customerID

    def getOnMailingList(self):
        """
        Returns the True if this Customer is on a Mailing otherwise returns False.

        :return: (bool) True if the Customer is on a Mailing otherwise returns False.
        """
        return self.__onMailingList

    def setOnMailingList(self, onMailingList):
        """
        Set the onMailingList to the given value.

        :param onMailingList: (bool) True if the Customer is on a Mailing otherwise returns False.

        :return: (None).
        """
        self.__onMailingList = onMailingList

    def __str__(self):
        """
        Returns the string representation of the Customer instance.

        :return: (str) The string representation of the Customer instance.
        """
        return super().__str__() + f"\nCustomer ID: {self.getCustomerID()} \nOn Mailing List: {self.getCustomerID()}"
