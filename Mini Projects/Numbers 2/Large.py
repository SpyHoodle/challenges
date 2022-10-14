def main():
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    digit = int(input("Enter a digit: "))

    assert 1 <= digit <= 9 and 0 < len(str(num_1)) <= 100 and 0 <= len(str(num_2)) <= 100
    count = 0
    product = str(num_1 * num_2)
    for d in product:
        if str(digit) == d:
            count += 1

    print(f"{digit} appears {count} times in {num_1} * {num_2}.")


if __name__ == "__main__":
    main()
