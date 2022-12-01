import colors as c


class Node:
    def __init__(self, data: str, next_node):
        self.data: str = data
        self.next: Node | None = next_node


class LinkedList:
    def __init__(self):
        self.nodes: list[Node] = []
        self.head: Node | None = None

    def __repr__(self):
        node = self.head
        linked_list = f"{c.cyan}LinkedList{c.blue}({c.end}"
        while node:
            linked_list += f"{node.data} {c.green}->{c.end} "
            node = node.next
        linked_list += f"{c.grey}None{c.blue}){c.end}"
        return linked_list

    def __len__(self):
        return len(self.nodes) + 1

    @staticmethod
    def _fatal(msg: str) -> None:
        print(f"{c.red}Error: {c.lightYellow}{msg}!{c.end}")
        exit(1)

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

    def remove(self, del_node: Node):
        if del_node in self.nodes:
            index = self.nodes.index(del_node)
            if self.nodes[index] == self.head:
                self.head = self.head.next
            else:
                self.nodes[self.nodes.index(self.node(self.index(del_node) - 1))].next = del_node.next
            self.nodes.pop(index)
        else:
            self._fatal(f"Failed to delete node '{del_node.data}' as it was not found in the linked list")

    def pop(self, del_node_index: int):
        self.remove(self.node(del_node_index))

    def node(self, index: int):
        if index < 0 or index > len(self.nodes) - 1:
            self._fatal(f"Failed to find note at index '{index}' as it is out of range")
        node = self.head
        count = 0
        while node:
            if count == index:
                return node
            else:
                node = node.next
            count += 1

    def index(self, find_node: Node):
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

    def swap(self, node1: Node, node2: Node):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[self.nodes.index(node1)].data, self.nodes[self.nodes.index(node2)].data = node2.data, node1.data

        else:
            self._fatal(f"Failed to swap nodes '{node1.data}' and '{node2.data}' "
                        f"as one or both of them do not exist within the linked list")

    def swap_index(self, index1: int, index2: int):
        self.swap(self.node(index1), self.node(index2))