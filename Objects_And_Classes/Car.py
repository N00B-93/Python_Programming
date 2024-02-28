from time import sleep


class Car(object):
    """
    A class representing a Car.

    Attributes:
        yearModel (int): The Car's year model.

        make (str): The Car's make.

        speed (int): The Car's speed.
    """
    def __init__(self, yearModel, make, speed):
        self.__yearModel = yearModel
        self.__make = make
        self.__speed = speed

    def getYearModel(self):
        """
        Returns the Car's year model.

        :return: (int) The Car's year model.
        """
        return self.__yearModel

    def setYearModel(self, yearModel):
        """
        Sets the Car's year model to the given value.

        :param yearModel: (int) The Car's year model.

        :return: None.
        """
        self.__yearModel = yearModel

    def getMake(self):
        """
        Returns the Car's make.

        :return: (str) The Car's make.
        """
        return self.__make

    def setMake(self, Make):
        """
        Sets the Car's make to the given value.

        :param Make: (str) The Car's make.

        :return: None.
        """
        self.__make = Make

    def getSpeed(self):
        """
        Returns the Car's current speed.

        :return: (int) The Car's current speed.
        """
        return self.__speed

    def setSpeed(self, speed):
        """
        Sets the Car's current speed to the given value.

        :param speed: (int) The Car's current speed value.

        :return: None.
        """
        self.__speed = speed

    def accelerate(self):
        """
        Increments the car's current speed by 5.

        :return: None.
        """
        self.__speed += 5

    def brake(self):
        """
        Decrements the car's current speed by 5.

        :return: None.
        """
        self.__speed -= 5


def main() -> None:
    # Creates a Car Object.
    car = Car(2000, "Mercedes", 0)

    # Accelerates the car 5 times and displays the car's current speed each time it is accelerated.
    print("\nAccelerating car...")
    sleep(2)
    for i in range(5):
        car.accelerate()
        print(f"\nThe current speed is: {car.getSpeed()}")

    # Decelerates the car 5 times and displays the car's current speed each time it is accelerated.
    print("\nApplying Brakes...")
    sleep(2)
    for i in range(5):
        car.brake()
        print(f"\nThe current speed is: {car.getSpeed()}")


if __name__ == "__main__":
    main()
