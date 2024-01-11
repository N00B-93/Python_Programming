from random import randint

"""
    This is a program that simulates picking a card from a deck of
    52 cards. The program displays the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
"""

# Generates a number from 1 to 13 that represents the rank of a card
rank = randint(1, 13)

# Generates a number from 1 to 4 that represents a card's suit.
suit = randint(1, 4)

# Matches a rank with the correct string representation.
match rank:
    case 1:
        rank = 'Ace'
    case 11:
        rank = 'Jack'
    case 12:
        rank = 'Queen'
    case 13:
        rank = 'King'

# Matches a suit with the correct string representation
match suit:
    case 1:
        suit = 'Clubs'
    case 2:
        suit = 'Diamonds'
    case 3:
        suit = 'Hearts'
    case 4:
        suit = 'Spades'

# Displays a random card.
print(f"\nThe Card you picked is: {rank} of {suit}")
