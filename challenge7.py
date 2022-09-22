from random import randint
from time import sleep


def reward(numbers, credit):
    # Check for two skull symbols
    if numbers[0] == numbers[1] == 5 or numbers[0] == numbers[2] == 5 or numbers[1] == numbers[2] == 5:
        print("You lost £1!")
        credit -= 1.00

    # Check for 3 skull symbols
    elif numbers[0] == numbers[1] == numbers[2] == 5:
        print(f"You lost all of your money!")
        credit = 0

    # Check for 2 of the same symbol
    if numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
        print("You won 50p!")
        credit += 0.50

    # Check for 3 of the same symbol
    elif numbers[0] == numbers[1] == numbers[2]:
        print("You won £1!")
        credit += 1.00

    # Check for 3 bell symbols
    elif numbers[0] == numbers[1] == numbers[2] == 1:
        print("You won £5!")
        credit += 10.00

    # Otherwise, the player doesn't win or loose
    else:
        print("You didn't win anything.")

    return credit


def roll(symbols, credit):
    # Press enter to roll
    input("\nPress enter to insert 20p.")

    # Subtract 20p from the credit
    print("20p inserted...")
    credit -= 0.20

    # Generate 3 random integers from 0 to 5
    numbers = [randint(0, 5) for _ in range(3)]

    # Show the symbols
    for number in numbers:
        print(f" {symbols[number]}", end="")
        sleep(0.5)
    print()

    # Check for reward or loss
    credit = reward(numbers, credit)

    return credit


def turn(symbols, credit):
    # Roll the symbols
    credit = roll(symbols, credit)

    # Check if the player has any money left
    if credit >= 0.20:
        # Ask the player if they want to play again
        print(f"\nYou have £{credit} left.")
        play_again = input("Do you want to play again? (y/N): ").upper()

        # If they say yes, run another turn
        if play_again == "Y" or play_again == "YES":
            turn(symbols, credit)

        # If they say no, end the game
        else:
            return credit

    # If the player doesn't have enough money, end the game
    else:
        return credit


def play(symbols, credit):
    credit = turn(symbols, credit)

    if credit:
        print(f"Thanks for playing! You have £{credit} left.")

    elif not credit:
        print("You do not have enough credit to play.")


def main():
    symbols = ["🍒", "🔔", "🍋", "🍊", "⭐", "💀"]
    credit = 1.00

    play(symbols, credit)


if __name__ == "__main__":
    main()
