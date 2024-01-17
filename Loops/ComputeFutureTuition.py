"""
    This is a program that computes the tuition in ten years
    and the total cost of four years’ worth of tuition starting after ten years from now.
    Assuming the current price is $ 10, 000 and it increases by 5% every year.
"""

# Initializes the variable holding the tuition after 10 years and the total tuition four years after the tenth year.
totalTuitionAfterTenthYear = 0
initialTuition = 10000
currentTuition = initialTuition + (initialTuition * 0.05)

for year in range(1, 14):
    # Calculates the current tuition for each year.
    currentTuition += currentTuition * 0.05

    # Displays the current tuition after ten years.
    if year == 9:
        print(f"\nThe tuition after 10 years is: $ {currentTuition:.2f}")

    # Calculates the total tuition for fours years after the tenth year.
    if year > 9:
        totalTuitionAfterTenthYear += currentTuition

# Displays the total tuition for fours years after the tenth year.
print(f"\nThe total tuition fours years after the tenth year is: $ {totalTuitionAfterTenthYear:.2f} ")


