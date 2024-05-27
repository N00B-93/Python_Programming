from sys import exit

"""
    In one version of Pig Latin, you convert a word by removing the first letter, placing that letter 
    at the end of the word, and then appending “ay” to the word.
    This program prompts the user to enter a sentence and then displays the Pig Latin equivalent.
"""


def toPigLatin(string):
    """
    Converts a given String to its Pig Latin equivalent.
    :param string: (str) The String to be converted to Pig Latin.

    :return: (str) The Pig Latin equivalent of a String.
    """
    letters = list(string)

    letters.append(letters.pop(0))

    pigLatin = ""

    for i in range(len(letters)):
        pigLatin += letters[i]

    if pigLatin.isupper():
        return pigLatin + 'AY '

    return pigLatin + 'ay '


def main() -> None:
    # Reads in a sentence.
    sentence = input("\nEnter a String to be converted: ")
    
    # Breaks the sentence into a list of Strings.
    words = sentence.split()
    
    # Displays the Pig Latin equivalent of a String that contains a single character and exits the program.
    if len(words) == 1 and len(words[0]) == 1:
        print(f"\nLetter: {words[0]}\nPig Latin {words[0] + 'ay'}")
        exit(0)

    pigLatin = ""
    
    # Converts each String in the words list to Pig Latin.
    for i in range(len(words)):
        pigLatin += toPigLatin(words[i])

    # Displays the result.
    print(f"\nSentence: {sentence}\n\nPig Latin: {pigLatin}")


if __name__ == "__main__":
    main()
