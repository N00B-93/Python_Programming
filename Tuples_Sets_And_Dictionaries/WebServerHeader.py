from urllib.request import urlopen

"""
    This is a program that prompts the user to enter the url to a web server and
    then displays the meta-data such as; the date the document was last modified, 
    the content type of the resource stored at the URL, etc,.
"""


def main() -> None:
    # Prompts the user to enter a URL to process.
    url: str = input("\nEnter a valid URL: ")
    # Checks if the URL starts with https://www and adds it if it doesn't.
    if not url.startswith("https://www."):
        url = "https://www." + url

    try:
        # Opens the URL.
        response = urlopen(url)

        # Returns the meta-data of the webserver as a dictionary.
        headerInformation: dict = response.getheaders()

        # Prints out the header information of the webserver.
        print()
        {print(f"{key}: {value}") for key, value in headerInformation}
    except Exception as exception:
        print()
        print(exception.__str__())

        
if __name__ == "__main__":
    main()

