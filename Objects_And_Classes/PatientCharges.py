class Patient:
    """
    A class to represent a Patient's Charges'.

    Attributes:
        fullName (str): The full name of the Patient.

        address (str): The address of the Patient.

        phoneNumber (str): The phone number of the Patient.

        zipCode (int): The zip code of the Patient.

        nameOfEmergencyContact (str): The name of the patient's emergency contact.

        phoneNumberOfEmergencyContact (str): The phone number of the patient's emergency contact.
    """
    def __init__(self, fullName, address, phoneNumber, zipCode, nameOfEmergencyContact, phoneNumberOfEmergencyContact):
        self.__fullName = fullName
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__zipCode = zipCode
        self.__nameOfEmergencyContact = nameOfEmergencyContact
        self.__phoneNumberOfEmergencyContact = phoneNumberOfEmergencyContact

    def getFullName(self):
        """
        Returns the full name of the Patient.

        :return: (str): The full name of the Patient.
        """
        return self.__fullName

    def setFullName(self, fullName):
        """
        Sets the full name of the Patient with the given full name.

        :param fullName: (str) The full name of the Patient.

        :return: (None).
        """
        self.__fullName = fullName

    def getAddress(self):
        """
        Returns the address of the Patient.

        :return: (str) The address of the Patient.
        """
        return self.__address

    def setAddress(self, address):
        """
        Sets the address of the Patient with the given address.

        :param address: (str) The address of the Patient.

        :return: (None).
        """
        self.__address = address

    def getPhoneNumber(self):
        """
        Returns the phone number of the Patient.

        :return: (str) The phone number of the Patient.
        """
        return self.__phoneNumber

    def setPhoneNumber(self, phoneNumber):
        """
        Sets the phone number of the Patient with the given phone number.

        :param phoneNumber: (str) The phone number of the Patient.

        :return: (None).
        """
        self.__phoneNumber = phoneNumber

    def getZipCode(self):
        """
        Returns the zip code of the Patient.

        :return: (str) The zip code of the Patient.
        """
        return self.__zipCode

    def setZipCode(self, zipCode):
        """
        Sets the zip code of the Patient with the given zip code.

        :param zipCode: (int) The zip code of the Patient.
        :return: (None).
        """
        self.__zipCode = zipCode

    def getNameOfEmergencyContact(self):
        """
        Returns the name of the Emergency contact of the Patient.

        :return: (str) The name of the Emergency contact of the Patient.
        """
        return self.__nameOfEmergencyContact

    def setNameOfEmergencyContact(self, nameOfEmergencyContact):
        """
        Sets the name of the Emergency contact of the Patient.

        :param nameOfEmergencyContact: (str) The name of the Emergency contact of the Patient.

        :return: (None).
        """
        self.__nameOfEmergencyContact = nameOfEmergencyContact

    def getPhoneNumberOfEmergencyContact(self):
        """
        Returns the phone number of the Emergency contact of the Patient.

        :return: (str) The phone number of the Emergency contact of the Patient.
        """
        return self.__phoneNumberOfEmergencyContact

    def setPhoneNumberOfEmergencyContact(self, phoneNumberOfEmergencyContact):
        """
        Sets the name of the phone number of the Emergency contact of the Patient.

        :param phoneNumberOfEmergencyContact: (str) The name of the phone number of the Emergency contact
        of the Patient.

        :return: (None).
        """
        self.__phoneNumberOfEmergencyContact = phoneNumberOfEmergencyContact


class Procedure:
    """
    A class that represents a Medical Procedure.

    Attributes:
        name (str): The name of the procedure.

        Date (str): The date of the procedure.

        nameOfPractitioner (str): The name of the procedure's practitioner.

        charges (float): The cost of the procedure.
    """
    def __init__(self, name, Date, nameOfPractitioner, charges):
        self.__name = name
        self.__Date = Date
        self.__nameOfPractitioner = nameOfPractitioner
        self.__charges = charges

    def getName(self):
        """
        Returns the name of the procedure.

        :return: (str) The name of the procedure.
        """
        return self.__name

    def setName(self, name):
        """
        Sets the name of the procedure with the given name.

        :param name: (str) The name of the procedure.

        :return: (None).
        """
        self.__name = name

    def getDate(self):
        """
        Returns the date of the procedure.

        :return: (str) The date of the procedure.
        """
        return self.__Date

    def setDate(self, Date):
        """
        Sets the date of the procedure with the given date.

        :param Date: (str) The date of the procedure.

        :return: (None).
        """
        self.__Date = Date

    def getNameOfPractitioner(self):
        """
        Returns the name of the procedure's Practitioner.

        :return: (str) The name of the procedure's Practitioner.
        """
        return self.__nameOfPractitioner

    def setNameOfPractitioner(self, nameOfPractitioner):
        """
        Sets the name of the procedure's Practitioner with the given name.

        :param nameOfPractitioner: (str) The name of the procedure's Practitioner.

        :return: (None).
        """
        self.__nameOfPractitioner = nameOfPractitioner

    def getCharges(self):
        """
        Returns the cost of the procedure.

        :return: (float) The cost of the procedure.
        """
        return self.__charges

    def setCharges(self, charges):
        """
        Sets the cost of the procedure's charges.

        :param charges: (float) The cost of the procedure.

        :return: (None).
        """
        self.__charges = charges


def main():
    # Creates three instance of a procedure.
    procedure1 = Procedure("General Exam", "15/01/2019", "Dr. Irvine",
                           250.0)
    procedure2 = Procedure("X-ray", "15/10/2019", "Dr. Jamison", 500.0)
    procedure3 = Procedure("Blood test", "15/10/2018", "Dr. Smith", 200.0)

    # Prompts the user to enter his/her full name.
    fullName = input("\nEnter your full name: ")

    # Prompts the user to enter his/her address.
    address = input("\nEnter your address: ")

    # Prompts the user to enter his/her zipcode.
    zipCode = int(input("\nEnter your zip code(e.g., 12345): "))

    # Prompts the user to enter his/her phone number.
    phoneNumber = input("\nEnter your phone number: ")

    # Prompts the user to enter the name of his/her emergency contact.
    nameOfEmergencyContact = input("\nEnter name of emergency contact: ")

    # Prompts the user to enter the phone number of his/her emergency contact.
    emergencyContactNumber = input("\nEnter your emergency contact's phone number: ")

    # Creates an instance of a Patient.
    patient = Patient(fullName, address, zipCode, phoneNumber, nameOfEmergencyContact, emergencyContactNumber)

    # Display's the patient's information.
    print("\n\t\tPatient's Information:")
    print(f"Patient's Full Name: {patient.getFullName()}\nPatient's address: {patient.getAddress()}"
          f"\nPatient's Zip Code: {patient.getZipCode()}\nPatient's phone number: {patient.getPhoneNumber()}"
          f"\nPatient's Emergency Contact: {patient.getNameOfEmergencyContact()}"
          f"\nPatient's Emergency Contact's phone number: {patient.getPhoneNumberOfEmergencyContact()}")

    # Display's all the Procedure Details.
    print("\n\t\tProcedure Details")
    print(f"Procedure Name: {procedure1.getName()}\nProcedure Date: {procedure1.getDate()}\n"
          f"Procedure Practitioner: {procedure1.getNameOfPractitioner()}\nCharges: $ {procedure1.getCharges()}")

    print(f"\nProcedure Name: {procedure2.getName()}\nProcedure Date: {procedure2.getDate()}\n"
          f"Procedure Practitioner: {procedure2.getNameOfPractitioner()}\nCharges: $ {procedure2.getCharges()}")

    print(f"\nProcedure Name: {procedure3.getName()}\nProcedure Date: {procedure3.getDate()}\n"
          f"Procedure Practitioner: {procedure3.getNameOfPractitioner()}\nCharges: $ {procedure3.getCharges()}")


if __name__ == "__main__":
    main()
