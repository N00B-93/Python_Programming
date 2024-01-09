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

# Prompts the user to enter the exchange rate between the two currencies.
exchangeRate = float(input("\nEnter the exchange rate from USD to RMB: "))

# Converts from one currency to the other and displays the result.
if choice == 0:
    amount = float(input("\nEnter the amount in dollars: "))
    chineseRMB = amount * exchangeRate
    print(f"\n{amount} USD = {chineseRMB} RMB")
elif choice == 1:
    amount = float(input("\nEnter the amount in yuan: "))
    americanUSD = amount / exchangeRate
    print(f"\n{amount} RMB = {americanUSD:.3f} USD")
