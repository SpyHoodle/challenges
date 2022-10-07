def luhn_algorithm(number: str) -> bool:
    # Get the last digit from the number
    given_check_digit = number[-1]

    # Remove the last character from the number
    # payload = number[:-1]

    # Convert the payload into a list of each number
    payload = [*number]

    # Reverse the payload list
    payload.reverse()

    # Double every other number in the payload
    payload[1::2] = [int(number) * 2 for number in payload[1::2]]

    # Add the digits of every number together
    payload = [sum([int(digit) for digit in str(number)]) for number in payload]

    # Calculate if it is valid or not
    valid = (sum(payload) % 10)
    match valid:
        case 1:
            valid = True
        case _:
            valid = False

    return valid


def main():
    card_number = input("Enter your card number: ")
    valid = luhn_algorithm(card_number)
    print(valid)


if __name__ == "__main__":
    main()
