def luhn_algorithm(number: int) -> bool:
    # Convert the payload into a list of each number
    payload = [*str(number)]

    # Reverse the payload list
    payload.reverse()

    # Double every other number in the payload
    payload[1::2] = [int(number) * 2 for number in payload[1::2]]

    # Add the digits of every number together
    payload = [sum([int(digit) for digit in str(number)]) for number in payload]

    # Get the remainder after dividing by 10
    mod_10 = sum(payload) % 10

    if mod_10 == 0:
        # If the remainder of mod 10 is 0, the number is valid
        return True

    else:
        # Otherwise, the card must be invalid
        return False


def main():
    # Print a title
    print("--- Card Number Validator ---")

    # Ask the user to enter a card number
    card_number = int(input("Enter the card number: "))

    # Check if the card is valid or not using the Luhn Algorithm
    valid = luhn_algorithm(card_number)

    # If the card is valid
    if valid:
        # Tell the user the card is valid
        print("The card number is valid.")

    # Otherwise, it must be invalid
    else:
        # Tell the user the card is invalid
        print("The card number is invalid.")


if __name__ == "__main__":
    main()
