import colors as c


class Queue:
    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self._head: int = 0
        self._tail: int = 0
        self._items = [None for _ in range(self.max_size)]

    def __str__(self):
        queue = f"{c.cyan}Queue{c.blue}({c.end}"
        for index, item in enumerate(self._items):
            if self._head == index:
                queue += f"{c.green}{item}{c.end}, "
            elif self._tail == index:
                queue += f"{c.red}{item}{c.end}, "
            elif item:
                queue += f"{item}, "
            else:
                queue += f"{c.grey}None{c.end}, "

        queue = queue[:-2]
        queue += f"{c.blue}){c.end}"
        if self._is_full():
            queue += f" {c.red}(Full){c.end}"
        elif self._is_empty():
            queue += f" {c.green}(Empty){c.end}"

        return queue

    def __len__(self):
        return len(self._items)

    @staticmethod
    def _fatal(msg: str) -> None:
        print(f"{c.red}Error: {c.lightYellow}{msg}!{c.end}")

    def _is_empty(self) -> bool:
        return self._head == self._tail

    def _is_full(self) -> bool:
        return self._head == self._tail or self._tail >= self.max_size

    def enqueue(self, item):
        if self._is_full():
            self._fatal(f"Cannot add item '{item}' as queue is full")
        else:
            if self._tail == self.max_size and self._head != 0:
                self._tail = 0
            self._items[self._tail] = item
            self._tail += 1

    def dequeue(self):
        if self._is_empty():
            self._fatal("There are no items to remove from the queue")
        else:
            self._head += 1
            if self._head == self.max_size:
                self._head = 0

    def get_head(self):
        if self._is_empty():
            self._fatal("There are no items in the queue")
        else:
            return self._items[self._head]

    def get_tail(self):
        if self._is_empty():
            self._fatal("There are no items in the queue")
        else:
            return self._items[self._tail]

    def clear(self):
        self._items = [None for _ in range(self.max_size)]
        self._head = 0
        self._tail = 0


def main():
    queue = Queue(5)
    print(queue)
    queue.enqueue("test")
    print(queue)
    queue.enqueue("test2")
    print(queue)
    queue.enqueue("test3")
    print(queue)
    queue.enqueue("test4")
    print(queue)
    queue.enqueue("test5")
    print(queue)
    queue.enqueue("test6")
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.enqueue("test6")
    print(queue)
    queue.enqueue("test7")
    print(queue)


if __name__ == "__main__":
    main()
