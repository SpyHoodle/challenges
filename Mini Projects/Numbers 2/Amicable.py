def sum_of_divisors(num: int) -> int:
    return sum(digit for digit in range(1, num) if num % digit == 0)


def is_amicable(num_1: int, num_2: int) -> bool:
    if num_1 == num_2:
        return False

    elif sum_of_divisors(num_1) == num_2 and sum_of_divisors(num_2) == num_1:
        return True


def main():
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))

    if is_amicable(num_1, num_2):
        print(f"{num_1} and {num_2} are amicable.")
    else:
        print(f"{num_1} and {num_2} are not amicable.")


if __name__ == "__main__":
    main()
