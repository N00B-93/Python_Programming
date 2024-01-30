class Fan:
    """
    A class representing a Fan.

    Attributes:

        speed (int): The speed of the fan.

        on (bool): Whether the fan should be on or off.

        radius (float): The radius of the fan.

        colour (str): The colour of the fan.
    """
    SLOW, MEDIUM, FAST = 1, 2, 3

    def __init__(self, speed=SLOW, on=False, radius=5.0, colour="blue"):
        """
        Initializes a new Fan object with the given parameters.

        :param speed: (int) The speed of the fan

        :param on: (bool): Whether the fan should be on or off.

        :param radius: (float): The radius of the fan.

        :param colour: (str): The colour of the fan.
        """
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__colour = colour

    def setSpeed(self, speed):
        """
        Sets the speed of the fan.

        :param speed: The speed of the fan.

        :return: None.
        """
        self.__speed = speed

    def getSpeed(self):
        """
        Returns the speed of the fan

        :return: (int) The speed of the fan.
        """
        return self.__speed

    def getOn(self):
        """
        Returns the state of the fan.

        :return: (bool) Whether the fan should be on or off
        """
        return self.__on

    def setOn(self, on):
        """
        Sets the state of the fan to on.

        :param on: (bool) Whether the fan should be on or off.

        :return: None
        """
        self.__on = on

    def setRadius(self, radius):
        """
        Sets the radius of the fan.

        :param radius: (float) The fan's radius.

        :return: None
        """
        self.__radius = radius

    def getRadius(self):
        """
        Returns the radius of the fan.

        :return: (float) The radius of the fan.
        """
        return self.__radius

    def setColour(self, colour):
        """
        Sets the colour of the fan.

        :param colour: (str) The colour of the fan.

        :return: None.
        """

        self.__colour = colour

    def getColour(self):
        """
        Returns the colour of the fan

        :return: (str) The colour of the fan.
        """
        return self.__colour


def main():
    # Creates two Fan Objects.
    fan1 = Fan(Fan.FAST, True, 10.0, "yellow")
    fan2 = Fan(Fan.MEDIUM, False, 5.0, "blue")

    # Displays the properties of fan1.
    print("\nFan1's Properties:")

    print(f"Speed: {fan1.getSpeed()}\nIs ON? {fan1.getOn()}\nRadius: {fan1.getRadius()}\nColour: {fan1.getColour()}",
          sep="")

    # Display's the properties of fan2.
    print("\nFan2's Properties:")

    print(f"Speed: {fan2.getSpeed()}\nIs ON? {fan2.getOn()}\nRadius: {fan2.getRadius()}\nColour: {fan2.getColour()}",
          sep="")


if __name__ == "__main__":
    main()
