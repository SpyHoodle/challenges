def error(message: str) -> None:
    print(f"Fatal: {message}")


def is_empty(stack_pointer: int) -> bool:
    if stack_pointer == 0:
        return True
    else:
        return False


def is_full(stack_pointer: int, size: int) -> bool:
    if stack_pointer >= size:
        return True
    else:
        return False


def push(stack: [], pointer: int, size: int, item) -> tuple[list, int]:
    if is_full(pointer, size):
        error("Stack is full!")
    elif is_empty(pointer):
        stack[0] = item
        pointer = 1
    else:
        stack[pointer] = item
        pointer += 1

    return stack, pointer


def pop(stack: [], pointer: int) -> tuple[list, int]:
    if is_empty(pointer):
        error("There are no items to remove from the stack!")
    else:
        pointer -= 1
        stack[pointer] = None

    return stack, pointer


def main():
    stack = ["memem", "testing!!", None]
    size = len(stack)
    pointer = 2

    stack, pointer = pop(stack, pointer)
    print(stack, pointer)


if __name__ == "__main__":
    main()
