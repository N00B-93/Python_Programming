class Pet:
    """
    A class representing a Pet.

    Attributes:
        name: (str) The name of the Pet.

        animalType: (str) The type of animal that the Pet is.

        age: (int): The age of the animal.
    """
    def __init__(self, name, animalType, age):
        self.__name = name
        self.__animalType = animalType
        self.__age = age

    def __str__(self):
        """
        Returns a String describing a Pet Object.

        :return: (str) Description of a Pet Object.
        """
        return f"Pet Name: {self.getName()}\nAnimal Type: {self.getAnimalType()}\nAge: {self.getAge()}"

    def setName(self, newName):
        """
        Sets the Pet's name to the given new name.

        :param newName: (str) The Pet's new name.

        :return: None.

        """
        self.__name = newName

    def getName(self):
        """
        Returns the name of the Pet.

        :return: (str) The Pet's name.
        """
        return self.__name

    def setAnimalType(self, newType):
        """
        Sets the Pet's animalType attribute to the given value.

        :param newType: (str) The new animal type.

        :return: None.
        """
        self.__animalType = newType

    def getAnimalType(self):
        """
        Returns the type of animal the Pet is.

        :return: (str) Animal Type of the Pet.
        """
        return self.__animalType

    def setAge(self, newAge):
        """
        Sets the Pet's age to the given value.

        :param newAge: (int) The Pet's new age.

        :return: None.
        """
        self.__age = newAge

    def getAge(self):
        """
        Returns the current Age of the Pet.

        :returns: (int) The Pet's age.
        """
        return self.__age


def main() -> None:
    try:
        # Reads in a Pet Object's name, animal type and age.
        name = input("\nEnter the Pet's name: ")

        animalType = input("\nEnter Animal Type: ")

        age = int(input("\nEnter Pet's age: "))

        pet = Pet(name, animalType, age)
        
        # Displays the Pet's Information.
        print("\n\t\tPet Information")
        print(pet.__str__())
    except ValueError:
        print("\nEnter the age as an integer!")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
