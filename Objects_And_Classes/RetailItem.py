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


def main():
    # Creates three RetailItem Objects.
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Prints Item details.
    print("\n\t\tItem Details.")
    print(f"Item Description: {item1.getDescription()}\nUnits In Inventory: {item1.getUnitsInInventory()}"
          f"\nItem Price: $ {item1.getPrice()}")
    print(f"\nItem Description: {item2.getDescription()}\nUnits In Inventory: {item2.getUnitsInInventory()}"
          f"\nItem Price: $ {item2.getPrice()}")
    print(f"\nItem Description: {item3.getDescription()}\nUnits In Inventory: {item3.getUnitsInInventory()}"
          f"\nItem Price: $ {item3.getPrice()}")


if __name__ == "__main__":
    main()
