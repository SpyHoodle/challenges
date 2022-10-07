def sum_of_squares_of_digits(num):
    return sum(int(digit) ** 2 for digit in str(num))


def is_happy_number(num):
    history = set()
    while num != 1:
        num = sum_of_squares_of_digits(num)
        if num in history:
            return False
        else:
            history.add(num)
    return True


def main():
    num = 0
    happy_nums = []
    while len(happy_nums) < 8:
        is_happy = is_happy_number(num)
        if is_happy:
            happy_nums.append(num)
        num += 1

    print(f"First {num} happy numbers:", happy_nums)


if __name__ == "__main__":
    main()
