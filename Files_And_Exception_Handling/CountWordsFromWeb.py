from urllib.request import urlopen

"""
    This is a program that counts the number of words in Abraham Lincoln's Gettysburg Address from;
            http://cs.armstrong.edu/liang/data/Lincoln.txt.
"""


def main() -> None:
    # Creates a URL object with a given url.
    url = "http://cs.armstrong.edu/liang/data/Lincoln.txt"
    try:
        # Connects to the Lincoln.txt file on the web.
        fileHandler = urlopen(url)
    
        # Reads and decode the content of the file.
        fileContent = fileHandler.read().decode("UTF-8")
    
        # Split the contents into a list of words.
        listOfWords = fileContent.split()
    
        # Displays the number of words in the file.
        print(f"\nThe number of words is: {len(listOfWords)}")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()
