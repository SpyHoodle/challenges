import colors as c


class Stack:
    def __init__(self, max_size: int):
        self.pointer: int = 0
        self.max_size: int = max_size
        self.items = [None for _ in range(self.max_size)]

    def __repr__(self):
        stack = f"{c.cyan}Stack{c.blue}({c.end}"
        for item in self.items:
            if item:
                stack += f"{item}{c.green},{c.end} "
            else:
                stack += f"{c.grey}None{c.green},{c.end} "

        stack = stack[:-2 - len(c.end) - len(c.green)]
        stack += f"{c.blue}){c.end}"

        return stack

    def __len__(self):
        return len(self.items)

    @staticmethod
    def _fatal(msg: str) -> None:
        print(f"{c.red}Error: {c.lightYellow}{msg}!{c.end}")
        exit(1)

    def is_empty(self) -> bool:
        if self.pointer == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.pointer >= self.max_size:
            return True
        else:
            return False

    def push(self, item):
        if self.is_full():
            self._fatal(f"Cannot add item '{item}' as stack is full")
        elif self.is_empty():
            self.items[0] = item
            self.pointer = 1
        else:
            self.items[self.pointer] = item
            self.pointer += 1

    def pop(self):
        if self.is_empty():
            self._fatal("There are no items to remove from the stack")
        else:
            self.pointer -= 1
            self.items[self.pointer] = None

    def clear(self):
        self.items = [None for _ in range(self.max_size)]
        self.pointer = 0


def main():
    stack = Stack(5)
    stack.push("memem")
    print(stack)
    stack.push("testing!!")
    print(stack)
    stack.push("testing!!")
    print(stack)
    stack.push("testing!!")
    print(stack)
    stack.push("testing!!")
    print(stack)
    print(stack)
    stack.pop()
    print(stack)
    stack.clear()
    print(stack)


if __name__ == "__main__":
    main()
