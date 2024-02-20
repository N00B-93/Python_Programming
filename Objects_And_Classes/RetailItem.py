class RetailItem:
    """
    A class representing a retail item.

    Attributes:
        description (str): The description of the retail item.

        unitsInInventory (int): The number of units in the inventory.

        price (float): The price of the retail item.
    """
    def __init__(self, description, unitsInInventory, price):
        self.__description = description
        self.__unitsInInventory = unitsInInventory
        self.__price = price

    def getDescription(self):
        """
        Returns the description of the retail item.

        :return: (str) The description of the retail item.
        """
        return self.__description

    def setDescription(self, description):
        """
        Sets the description of the retail item to the given description.

        :param description: (str) The description of the retail item.

        :return: (None).
        """
        self.__description = description

    def getUnitsInInventory(self):
        """
        Returns the number of units of an item in the inventory.

        :return: (int) The number of units of an item in the inventory.
        """
        return self.__unitsInInventory

    def setUnitsInInventory(self, unitsInInventory):
        """
        Sets the number of units of an item in the inventory to the given units.

        :param unitsInInventory: (int) The number of units of an item in the inventory.

        :return: (None).
        """
        self.__unitsInInventory = unitsInInventory

    def getPrice(self):
        """
        Returns the price of the retail item.

        :return: (float) The price of the retail.
        """
        return self.__price

    def setPrice(self, price):
        """
        Sets the price of the retail item to the given price.

        :param price: (float) The price of the retail item.

        :return: (None)
        """
        self.__price = price

