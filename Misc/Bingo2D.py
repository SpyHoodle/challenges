from random import randint


def generate_ticket(length: int, height: int) -> list[list]:
    ticket = []
    for i in range(height):
        empty_pos = set()
        while len(empty_pos) != 4:
            empty_pos = set(randint(0, length) for _ in range(4))
        row = []
        for j in range(length):
            if j in empty_pos:
                row.append("  ")
            else:
                row.append(str(randint(0, 99)).zfill(2))
        ticket.append(row)
    return ticket


def print_ticket(ticket: list[list]) -> None:
    print("Your ticket is:\033[37m")
    print("┌" + "┬".join("──" for _ in range(len(ticket[0]))) + "┐")
    for i, row in enumerate(ticket):
        for j, num in enumerate(row):
            print(f"│\033[32m{num}\033[37m", end="")
            if j == len(row) - 1:
                print("│")
        if not i == len(ticket) - 1:
            print("├" + "┼".join("──" for _ in range(len(row))) + "┤")
    print("└" + "┴".join("──" for _ in range(len(ticket[0]))) + "┘")


def main():
    ticket = generate_ticket(9, 3)
    print_ticket(ticket)


if __name__ == "__main__":
    main()
