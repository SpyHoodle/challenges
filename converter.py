def convert(number: int, base_to: int) -> int:
    return int(str(number), base_to)


def repeated_division(number: int):
    x = 0
    nums = []
    while number > 0:
        # Generate numbers 2**0, 2**1, 2**2, 2**3, ...
        div = [2**i for i in range(len(bin(number)))]
        n = number % div[x]
        nums.append(n)
        print(number)
    print(nums)


def main():
    mode = input("Mode: ")
    match mode:
        case "convert":
            base_from = int(input("Convert from base: "))
            base_to = int(input("Convert to base: "))

            number = int(input("Number: "), base_from)
            print(convert(number, base_to))
        case "rd":
            number = int(input("Number: "))
            print(repeated_division(number))


if __name__ == "__main__":
    main()
