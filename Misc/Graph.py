import colors as c  # noqa: F401


class Edge:
    def __init__(self, end, weight: int):
        self.end: Node = end
        self.weight: int = weight


class Node:
    def __init__(self, data: str, connections: [Edge] = None):
        self.data = data
        self.edges: [Edge] = connections or []

    def __str__(self):
        return str(self.data)


class Graph:
    def __init__(self):
        self.nodes: [Node] = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, start: Node, end: Node, weight: int):
        start.edges.append(Edge(end, weight))
        if start in self.nodes:
            self.nodes[self.nodes.index(start)] = start
        else:
            self.nodes.append(start)

    def remove_edge(self, start: Node, end: Node):
        for index, edge in enumerate(start.edges):
            if edge.end == end:
                start.edges.pop(index)
                break

        if start in self.nodes:
            self.nodes[self.nodes.index(start)] = start
        else:
            self.nodes.append(start)

    def remove_node(self, node: Node):
        self.nodes.remove(node)
        for n in self.nodes:
            for index, edge in enumerate(n.edges):
                if edge.end == node:
                    n.edges.pop(index)
                    break

    def __str__(self):
        graph = f"{c.cyan}Graph{c.blue}({c.end}"
        for node in self.nodes:
            graph += f"\n   [{c.green}{node}{c.end} -> "
            for edge in node.edges:
                graph += f"{c.green}{edge.end}{c.lightYellow}({c.red}{edge.weight}{c.lightYellow}){c.end} -> "
            graph += f"{c.grey}End{c.end}],"
        graph += f"\n{c.blue}){c.end}"
        return graph


def main():
    graph = Graph()
    a = Node("A", [Edge(Node("memememem"), 1000), Edge(Node("C"), 2)])
    c = Node("HelloWorld")
    b = Node("B", [Edge(c, 5)])
    graph.add_node(a)
    graph.add_node(b)
    print(graph)


if __name__ == "__main__":
    main()
