import threading

def next_num(num: int) -> int:
    return num + sum(int(i) for i in str(num))


def meets_at(num_1: int, num_2: int) -> int:
    while num_1 != num_2:
        if num_1 > num_2:
            num_2 = next_num(num_2)
        elif num_2 > num_1:
            num_1 = next_num(num_1)

    return num_1


def main():
    num = int(input("Enter a number: "))

    if 1 <= num <= 16384:
        threading.Thread(target=print(f"{num} meets 1 at: ", meets_at(num, 1))).start()
        threading.Thread(target=print(f"{num} meets 3 at: ", meets_at(num, 3))).start()
        threading.Thread(target=print(f"{num} meets 9 at: ", meets_at(num, 9))).start()


if __name__ == "__main__":
    main()
