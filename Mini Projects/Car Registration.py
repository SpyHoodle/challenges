
from datetime import datetime


def check_invalid_chars(string, invalid_chars):
    # Iterate through all invalid characters
    for char in invalid_chars:
        # Check if the string contains an invalid character
        if char in string:
            # If it does, the string is invalid
            return False

    # If the string does not contain any invalid characters, the string must be valid, therefore return True
    return True


def check_reg(car_registration):
    # Check if the car registration is 8 characters long
    if not len(car_registration) == 8:
        # If it isn't, then the car registration is invalid
        print("Error: Invalid car registration format, it must be 8 characters long.")

    # Check if digits 1 to 2 contain invalid characters or numbers
    elif not check_invalid_chars(car_registration[:2], ["I", "Q", "Z"]) or not car_registration[:2].isalpha():
        # If it does, the car registration is invalid
        print(f"Error: The first two digits must not contain I, Q, Z or any numerical character.")
        return False

    # Check if the second two digits are numbers
    elif not car_registration[2:4].isnumeric():
        # If it does, the car registration is invalid
        print(f"Error: The second two digits must be numerical digits.")
        return False

    # Check if the 5th digit contains an empty space
    elif not car_registration[4] == " ":
        # If it does, the car registration is invalid
        print(f"Error: The fifth digit must be a space character.")
        return False

    # Check if digits 6 to 8 contain invalid characters or numbers
    elif not check_invalid_chars(car_registration[5:8], ["I", "Q"]) or not car_registration[5:8].isalpha():
        # If it does, the car registration is invalid
        print(f"Error: Digits 6, 7 & 8 must not contain I, Q, or any numerical characters.")
        return False

    else:
        # If it has passed all checks, the car registration must be valid, therefore return it for use
        return car_registration


def check_car_year(car_year):
    # Check if the input was an integer and 4 characters long
    if car_year.isnumeric() and len(car_year) == 4:
        # Change the input to type int
        car_year = int(car_year)

    else:
        # The car year is invalid if it isn't an integer and contains alphabetical characters,
        # or isn't 4 characters long
        print(f"Error: Invalid car year format. Please try entering in the format YYYY.")
        return False

    # Check if the car's registration year was below 2002
    if car_year < 2002:
        # This program uses rules set after 2002, therefore cars registered before that year cannot be used
        print(f"Error: This program will not work with cars registered before 2002.")
        return False

    # Check if the car's year is above the current year
    elif car_year > datetime.now().year:
        # Impossible for a car to be registered in the future
        print(f"Error: Car cannot be registered above the current year.")
        return False

    else:
        # If it has passed all checks, the car's registration year must be valid, therefore return it for use
        return car_year


def main():
    owner_name = input("What is your legal name (FIRSTNAME SECONDNAME)? ")
    owner_number = input("What is your UK phone number (exclude +44) ? ")

    # Loop until the user gives a valid car registration year
    car_year = False
    while not car_year:
        # Get the car's registration year from the user
        car_year = input("Enter the year your car was registered (YYYY): ")

        # Check the car's registration year to see if it's valid
        car_year = check_car_year(car_year)

    # Loop until the user gives a valid car registration
    car_registration = False
    while not car_registration:
        # Get the car registration from the user
        car_registration = input("What is your car registration plate (XX00 XXX)? ").upper()

        # Check the car's registration to see if it's valid
        car_registration = check_reg(car_registration)


if __name__ == "__main__":
    main()
