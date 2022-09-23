from random import randint
from time import sleep


# Define colour codes
colours = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "clear": "\033[0m"
}


def reward(numbers, credit):
    # Check for two skull symbols
    if numbers[0] == numbers[1] == 5 or numbers[0] == numbers[2] == 5 or numbers[1] == numbers[2] == 5:
        print(f"{colours['red']}You lost £1!{colours['clear']}")
        credit -= 1.00

    # Check for 3 skull symbols
    elif numbers[0] == numbers[1] == numbers[2] == 5:
        print(f"{colours['red']}You lost all of your money!{colours['clear']}")
        credit = 0

    # Check for 3 bell symbols
    elif numbers[0] == numbers[1] == numbers[2] == 1:
        print(f"{colours['green']}You won £5!{colours['clear']}")
        credit += 10.00

    # Check for 3 of the same symbol
    elif numbers[0] == numbers[1] == numbers[2]:
        print(f"{colours['green']}You won £1!{colours['clear']}")
        credit += 1.00

    # Check for 2 of the same symbol
    elif numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
        print(f"{colours['green']}You won 50p!{colours['clear']}")
        credit += 0.50

    # Otherwise, the player doesn't win or loose
    else:
        print("You didn't win anything.")

    return credit


def roll(symbols, credit):
    # Print the title
    print(f"\n{colours['magenta']}🎰 Slot machine! 🎰{colours['clear']}")

    # Press enter to roll
    input(f"{colours['cyan']}Press enter to insert 20p.{colours['clear']}")

    # Subtract 20p from the credit
    print(f"{colours['blue']}20p inserted...{colours['clear']}")
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
        print(f"\n{colours['blue']}You have £{credit:.2f} left.")
        play_again = input(f"{colours['cyan']}Do you want to play again? (Y/n): ").upper()

        # If they say yes, run another turn
        if play_again == "N" or play_again == "NO":
            return credit

        # If they say no, end the game
        else:
            turn(symbols, credit)

    # If the player doesn't have enough money, end the game
    else:
        return credit


def play(symbols, credit):
    credit = turn(symbols, credit)

    if credit:
        print(f"{colours['magenta']}Thanks for playing! You have £{credit:.2f} left.{colours['clear']}")

    elif not credit:
        print(f"{colours['red']}You do not have enough credit to play.{colours['clear']}")


def main():
    symbols = ["🍒", "🔔", "🍋", "🍊", "⭐", "💀"]
    credit = 1.00

    play(symbols, credit)


if __name__ == "__main__":
    main()
