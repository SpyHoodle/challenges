class Colors:
    grey = "\033[0;37m"
    red = "\033[0;31m"
    lightYellow = "\033[1;33m"
    end = "\033[0m"


class Node:
    def __init__(self, data: str, next_node):
        self.data: str = data
        self.next: Node | None = next_node


class LinkedList:
    def __init__(self):
        self.nodes: list[Node] = []
        self.head: Node | None = None

    @staticmethod
    def _fatal(msg: str) -> None:
        print(f"{Colors.red}Error: {Colors.lightYellow}{msg}!{Colors.end}")
        exit(1)

    def __repr__(self):
        node = self.head
        linked_list = "["
        while node:
            linked_list += f"{node.data} -> "
            node = node.next
        linked_list += f"{Colors.grey}None{Colors.end}]"
        return linked_list

    def add(self, new_node: Node):
        if new_node.next == self.head:
            self.head = new_node
            self.nodes.append(new_node)
        elif new_node.next in self.nodes:
            for index, node in enumerate(self.nodes):
                if node.next == new_node.next:
                    self.nodes[index].next = new_node
            self.nodes.append(new_node)
        elif not new_node.next:
            for index, node in enumerate(self.nodes):
                if not node.next:
                    self.nodes[index].next = new_node
            self.nodes.append(new_node)
        else:
            self._fatal(f"Failed to add node '{new_node.data}' as next node '{new_node.next.data}' does not exist")

    def delete(self, del_node: Node):
        if del_node in self.nodes:
            index = self.nodes.index(del_node)
            if self.nodes[index] == self.head:
                self.head = self.head.next
            else:
                self.nodes[self.nodes.index(self.node_at_index(self.index_of_node(del_node) - 1))].next = del_node.next
            self.nodes.pop(index)
        else:
            self._fatal(f"Failed to delete node '{del_node.data}' as it was not found in the linked list")

    def node_at_index(self, index: int):
        if index < 0 or index > len(self.nodes) - 1:
            self._fatal(f"Index '{index}' out of range")
        node = self.head
        count = 0
        while node:
            if count == index:
                return node
            else:
                node = node.next
            count += 1

    def index_of_node(self, find_node: Node):
        if find_node in self.nodes:
            node = self.head
            count = 0
            while node:
                if node == find_node:
                    return count
                else:
                    count += 1
                node = node.next
        else:
            self._fatal(f"Failed to find index of node {find_node.data} as it does not exist within the linked list")


ll = LinkedList()
ll.add(Node("HewwoEvie:3", None))
print(ll)
ll.add(Node("DogsDinner!!", ll.node_at_index(0)))
print(ll)
ll.add(Node("CatsBreakfast!!!", ll.node_at_index(1)))
print(ll)
ll.delete(ll.node_at_index(1))
print(ll)
ll.delete(ll.node_at_index(0))
print(ll)
