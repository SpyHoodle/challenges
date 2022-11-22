class Node:
    def __init__(self, data: str, pointer: int):
        self.data: str = data
        self.pointer: int = pointer


class LinkedList:
    def __init__(self):
        self.nodes: list[Node] = []

    def add(self, node: Node):
        if node.pointer > len(self.nodes) - 1:
            node.pointer = -1
            if len(self.nodes) > 1:
                print(f"Node {node.data} points to {node.pointer} ({self.nodes[node.pointer].data})")
                self.nodes[-2].pointer = len(self.nodes)
        self.nodes.append(node)
        for i, snode in enumerate(self.nodes):
            if snode.pointer == node.pointer:
                snode.pointer = self.nodes.index(node)

    def print(self):
        for node in self.nodes:
            print(f"{node.data} -> {node.pointer} ({self.nodes[node.pointer - 1].data})")


ll = LinkedList()
ll.add(Node("World", 1))
ll.add(Node("Test", 3))
ll.add(Node("Experiment", 3))
ll.print()
