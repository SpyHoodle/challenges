def denary_int_to_binary(denary: int) -> int:
    binary = []
    while denary > 0:
        binary.append(denary % 2)
        denary = denary // 2
    binary = int("".join([str(digit) for digit in binary]))
    return binary


def binary_int_to_denary(binary: int) -> int:
    denary = 0
    for i, digit in enumerate(str(binary)[::-1]):
        denary += int(digit) * 2 ** i
    return denary


def main():
    bd_or_db = input("(B)inary to Denary or (D)enary to Binary? ").upper()

    match bd_or_db:
        case "B":
            binary = int(input("Enter a binary number: "))
            denary = binary_int_to_denary(binary)
            print(f"Your denary number is: {denary}")

        case "D":
            denary = int(input("Enter a denary number: "))
            binary = denary_int_to_binary(denary)
            print(f"Your binary number is: {binary}")


if __name__ == "__main__":
    main()
