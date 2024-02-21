from RetailItem import RetailItem


class CashRegister:
    """
    A class representing a Cash Register Object.

    Attributes:
        
        purchasedItems (list): A list containing RetailItem Objects.
    """
    def __init__(self, purchasedItems):
        self.purchasedItems = purchasedItems

    def purchaseItem(self, retailItem):
        """
        Adds a RetailItem Object to the purchasedItems list 

        :param retailItem: (RetailItem) The Object to be added to the list.

        :return: (None).
        """
        self.purchasedItems.append(retailItem)

    def getTotal(self):
        """
        Returns the total price of all retail item in the purchasedItem list.

        :return: (float) Total price of a retail items.
        """
        total = 0

        for item in self.purchasedItems:
            total += item.getPrice()

        return total

    def clearCart(self):
        """
        Clears the purchasedItems list.

        :return: (None)
        """
        self.purchasedItems.clear()
    
    def showItems(self):
        """
        Shows information about a retail item in the purchasedItems list.

        :return: (str) Information about the retailItem.
        """
        return (f"\nDescription: {self.purchasedItems.getDescription()}\nUnits In Inventory: "
                f"{self.purchasedItems.getUnitsInInventory()}\nPrice: {self.purchasedItems.getPrice()}")


def main():
    # Creates three RetailItem Objects.
    item1 = RetailItem("Faded Jean", 45, 21.25)
    item2 = RetailItem("Hoodie", 52, 35.21)
    item3 = RetailItem("Leather Jacket", 11, 45.60)
    item4 = RetailItem("Baseball Cap", 10, 9.12)
    item5 = RetailItem("Nike Air Jordan", 8, 101.28)

    # Creates a list to represent an empty cart.
    cart = []

    while True:
        print("\n\t\tAvailable Items")
        print(f"1. {item1.getDescription()}\t\t$ {item1.getPrice()}\n2. {item2.getDescription()}"
              f"\t\t\t$ {item2.getPrice()}\n3. {item3.getDescription()}\t$ {item3.getPrice()}\n"
              f"4. {item4.getDescription()}\t\t$ {item4.getPrice()}\n5. {item5.getDescription()}\t$ "
              f"{item5.getPrice()}\n6. Exit Menu")
        choice = input("\nEnter choice: ")

        match choice:
            case '1':
                cart.append(item1)
                print(f"\n{item1.getDescription()} added to cart!")
            case '2':
                cart.append(item2)
                print(f"\n{item2.getDescription()} added to cart!")
            case '3':
                cart.append(item3)
                print(f"\n{item3.getDescription()} added to cart!")
            case '4':
                cart.append(item4)
                print(f"\n{item4.getDescription()} added to cart!")
            case '5':
                cart.append(item5)
                print(f"\n{item5.getDescription()} added to cart!")
            case '6':
                break
            case _:
                print("\nInvalid option!")
    
    # Creates a CashRegister Object.
    cashRegister = CashRegister(cart)

    # Displays the items in the cart.
    print("\n\t\tItems in Cart:")
    print("\nItem Name\t\tQty")
    for items in cashRegister.purchasedItems:
        print(f"\n{items.getDescription()}\t\t{cart.count(items)}")
    
    # Displays the total price of all items in the cart.
    total = 0

    # Determines the cost of all items in the
    for item in cart:
        total += item.getPrice()

    # Displays the total price of all the items in the cart.
    print(f"\nThe total price of all items in the cart is: $ {total:.2f}")


if __name__ == "__main__":
    main()
