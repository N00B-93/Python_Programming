"""
    This is a program that prompts the user to enter
    the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
    It prompts the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
    vice versa. It also prompts the user to enter the amount in U.S. dollars or Chinese RMB to
    convert it to Chinese RMB or U.S. dollars, respectively.
"""

# Prompts the user to enter a conversion choice.
print("\n0. USD to RMB\n1. RMB to USD")
choice = int(input("\nEnter a choice: "))

# Displays an error message and terminates the program if the user enters an invalid choice.
if choice < 0 or choice > 1:
    print("\nError: Invalid input, Try again.")
    exit(1)

# Prompts the user to enter the exchange rate between the two currencies.
exchangeRate = float(input("\nEnter the exchange rate from USD to RMB: "))

# Displays an error message and terminates the program if the user enters an invalid exchange rate.
if exchangeRate <= 0:
    print("\nError: Exchange rate must be > 0.0, Try again.")
    exit(2)

if choice == 0:
    amount = float(input("\nEnter the amount in dollars: "))

    # Displays an error message and terminates the program if the amount entered by the user is <= $0.0
    if amount <= 0:
        print("\nError: Amount to be converted must be > 0.0, Try again.")
        exit(3)

    # Converts the amount to RMB and displays the result.
    chineseRMB = amount * exchangeRate
    print(f"\n{amount} USD = {chineseRMB} RMB")
elif choice == 1:
    amount = float(input("\nEnter the amount in yuan: "))

    # Displays an error message and terminates the program if the amount entered by the user is <= 0.0 RMB.
    if amount <= 0:
        print("\nError: Amount to be converted must be > 0.0, Try again.")
        exit(3)
    # Converts the amount to USD and displays the result.
    americanUSD = amount / exchangeRate
    print(f"\n{amount} RMB = {americanUSD:.3f} USD")
