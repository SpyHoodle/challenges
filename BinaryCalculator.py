def denary_to_binary(denary: int) -> int:
    binary = []
    while denary > 0:
        binary.append(denary % 2)
        denary = denary // 2
    binary = int("".join([str(digit) for digit in binary]))
    return binary


def binary_to_denary(binary: int, abd_mode: bool = True) -> int:
    if abd_mode:
        denary = 0
        for i, digit in enumerate(str(binary)[::-1]):
            denary += int(digit) * 2 ** i
        return denary

    else:
        return int(str(binary), 2)


def main():
    inp = input("(B)inary to Denary or (D)enary to Binary? ").upper()

    match inp:
        case "B":
            binary = int(input("Enter a binary number: "))
            denary = binary_to_denary(binary)
            print(f"Your denary number is: {denary}")

        case "D":
            denary = int(input("Enter a denary number: "))
            binary = denary_to_binary(denary)
            print(f"Your binary number is: {binary}")


if __name__ == "__main__":
    main()
