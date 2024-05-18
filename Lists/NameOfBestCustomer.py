
"""
    A supermarket wants to reward its best customer of each day, showing the customer’s name on a screen
    in the supermarket. For that purpose, the customer’s purchase amount is stored in a list and the
    customer’s name is stored in a corresponding list.
    This is a program prompts the cashier to enter all prices and names, adds them to two lists, input
    stops when the cashier enters 0 as purchase amount and the customer with the largest purchase is displayed.
"""


def getNamesOfBestCustomers(purchaseAmount: [float], customersNames: [str]) -> list[str]:
    """
    This determines the customer(s) that has the highest purchase amount's name.

    :param purchaseAmount: (list) A list containing the customers purchase amount.
    :param customersNames: (list) A list containing customers names.
    :return: (list) The name of the customer(s) with the highest purchase amount.
    """
    maxPurchase = max(purchaseAmount)

    bestCustomers = [customersNames[name] for name, purchase in enumerate(purchaseAmount) if purchase == maxPurchase]

    return bestCustomers


def main() -> None:
    # List to hold purchase amount and customer's names.
    purchaseAmount: [float] = []
    customersNames: [str] = []
    
    # Continues to prompt the cashier to enter name and purchase amount till the cashier enters a purchase amount of 0.
    print("\nEnter purchase amounts and customer names (enter 0 as purchase amount to stop)")
    while True:
        amount = float(input("\nEnter purchase amount: £"))
        
        # Breaks out of the loop if cashier enters purchase amount of 0.
        if amount == 0:
            break
        elif amount < 0:  # Continues to the next iteration if the cashier enters a negative amount.
            print("\nError: Invalid amount, Try again.")
            continue

        name = input("\nEnter customer name: ")
        
        # Continues to the next iteration if the cashier enters an invalid name.
        if name == '':
            print("\nError: Invalid name, Try again.")
            continue
        
        # Appends the customer's name and purchase amount to the name and purchase amount list.
        purchaseAmount.append(amount)
        customersNames.append(name)
    
    # Determines the customers with the highest purchase amounts.
    bestCustomers = getNamesOfBestCustomers(purchaseAmount, customersNames)

    # Displays the customers with the highest purchase amount.
    print("\nCustomer(s) with the highest purchase amount are: ")
    [print(bestCustomers[i]) for i in range(len(bestCustomers))]


if __name__ == "__main__":
    main()
