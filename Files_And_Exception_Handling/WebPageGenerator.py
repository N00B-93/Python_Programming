"""
    This is a program that asks the user to enter his/her name and prompts the user to enter a description of
    himself/herself. The program then generate an HTML file containing the user input for a simple webpage.
"""


def main() -> None:
    # Prompts the user to enter his/her name.
    name = input("\nEnter your name: ")

    # Prompts the user to describe himself/herself.
    description = input("\nDescribe yourself: ")

    # Creates a String that contains the user input and HTML code.
    HTMLContent: str = f"""
                            <html>
                                <head>
                                </head>
                                <body>
                                    <center>
                                        <h1>{name}</h1>
                                    </center>
                                    <hr />
                                    {description}
                                    <hr />
                                </body>
                            </html>"""

    try:
        # Writes the data to the file.
        with open("test.html", "w") as fileHandler:
            fileHandler.write(HTMLContent)
            print("\nHTML File Created Successfully")
    except Exception as exception:
        print(exception.__str__())


if __name__ == "__main__":
    main()
