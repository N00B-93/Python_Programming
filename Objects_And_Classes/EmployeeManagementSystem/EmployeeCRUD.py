from pickle import dump, load
from Employee import Employee
from time import sleep
from sys import exit


def addEmployee(employees):
    """
    Adds a new Employee to the EmployeeDetails file.

    :param employees: (dict) The EmployeeDetails dictionary.

    :return: None
    """
    fileHandler = None

    try:
        fileHandler = open('EmployeeDetails.dat', 'ab')

        employeeName = input("\nEnter your name: ")

        employeeID = int(input("\nEnter 5-digit ID number(e.g., 12345): "))

        while len(str(employeeID)) != 5:
            print("\nInvalid ID number. Use a 5-digit number.")
            employeeID = int(input("\nEnter 5-digit ID number(e.g., 12345): "))

        employeeJobTitle = input("\nEnter your Job Title: ")

        department = input("\nEnter your Department: ")

        employee = Employee(employeeName, employeeID, department, employeeJobTitle)

        employees.update({employee.getEmployeeID(): employee})

        dump(employees, fileHandler)

        print(f"\n{employeeName} has been Successfully Added!")
    except ValueError:
        raise ValueError(f"\nInvalid Employee ID!\nUse a valid ID(e.g., 12345)")
    except Exception as exception:
        raise exception
    finally:
        fileHandler.close()


def searchEmployee():
    """
    Search for an Employee in the EmployeeDetails file.

    :return: None
    """
    fileHandler = None

    try:
        fileHandler = open("EmployeeDetails.dat", "rb")

        employeeID = int(input("\nEnter 5-digit ID number(e.g., 12345): "))

        employees: dict = load(fileHandler)

        employee = employees.get(employeeID)

        if employee is not None:
            print("\nEmployee Found!")
        else:
            print("\nEmployee Not Found!")
            return

        print(employee.__str__())
    except Exception as exception:
        raise exception
    finally:
        fileHandler.close()


def updateEmployeeDetails():
    """
    Updates an Employee's Job title or Department.

    :return: None.
    """
    try:
        fileHandler = open("EmployeeDetails.dat", "rb")

        employees: dict = load(fileHandler)

        fileHandler.close()

        print("""\nWhat would you like to Update?
                    \n1. Employee Job Title
                    \n2. Employee Department
            """)
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                employeeID = int(input("\nEnter employee ID(e.g., 12345): "))

                newJobTitle = input("\nEnter new Job Title: ")

                employee = employees[employeeID]

                employee.setJobTitle(newJobTitle)

                print(f"\nJob Title changed to {newJobTitle}")

                with open("EmployeeDetails.dat", "wb") as fileHandler:
                    dump(employees, fileHandler)
            case '2':
                employeeID = int(input("\nEnter employee ID(e.g., 12345): "))

                newDepartment = input("\nEnter new Department Name: ")

                employee = employees[employeeID]

                employee.setDepartment(newDepartment)

                print(f"\nDepartment changed to {newDepartment}")

                with open("EmployeeDetails.dat", "wb") as fileHandler:
                    dump(employees, fileHandler)
            case '_':
                print("\nInvalid choice!")
    except KeyError:
        raise KeyError("Employee Not Found!")
    except ValueError:
        raise ValueError(f"Invalid Employee ID\nEnter a valid ID(e.g., 12345)")
    except Exception as exception:
        raise exception


def deleteEmployee():
    """
    Delete an Employee from the EmployeeDetails.dat file.

    :return: None.
    """
    try:
        fileHandler = open("EmployeeDetails.dat", 'rb+')

        employeeID = int(input("\nEnter 5-digit Employee ID: "))

        employees: dict = load(fileHandler)

        fileHandler.close()

        employee = employees.pop(employeeID)

        print(f"\n{employee.getEmployeeName()} Deleted Successfully!")

        with open("EmployeeDetails.dat", 'wb') as fileHandler:
            dump(employees, fileHandler)
    except KeyError:
        raise KeyError("Employee Not Found!")
    except ValueError:
        raise ValueError(f"Invalid Employee ID\nEnter a valid ID(e.g., 12345)")
    except Exception as exception:
        raise exception


def main() -> None:
    # Creates a Dictionary to hold Employee Objects.
    employees = {}

    print("\n\t\t\tWelcome to Employee Management System(EMS)")
    while True:
        # Displays the Menu.
        print("\nWhat would you like to?")
        print("""\n1. Add a new Employee.
                 \n2. Search for an Employee
                 \n3. Update Employee Details.
                 \n4. Delete an Employee.
                 \n5. Exit
                """)
        choice = input("\nEnter your choice: ")  # Reads in user's choice.

        match choice:
            case '1':
                try:
                    addEmployee(employees)
                except Exception as exception:
                    print(exception)
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '2':
                try:
                    searchEmployee()
                except Exception as exception:
                    print(exception)
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '3':
                try:
                    updateEmployeeDetails()
                except Exception as exception:
                    print(exception)
                choice = input("\nWould you like to continue? ('y' for yes, 'n' for no): ")
                if choice == 'y':
                    continue
                else:
                    exit(0)
            case '4':
                try:
                    deleteEmployee()
                except Exception as exception:
                    print(exception)
            case '5':
                print("\nExiting...", end="")
                sleep(2)
                exit(0)


if __name__ == '__main__':
    main()
