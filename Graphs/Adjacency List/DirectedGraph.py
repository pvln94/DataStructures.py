class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)
        self.graph[start].append(end)

    def remove_edge(self, start, end):
        if start in self.graph and end in self.graph[start]:
            self.graph[start].remove(end)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(map(str, self.graph[vertex]))}")

# Example usage
dg = DirectedGraph()
dg.add_edge(1, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 4)
dg.add_edge(3, 4)
dg.add_edge(4, 5)

print("Directed Graph:")
dg.display()

# Removing an edge
dg.remove_edge(3, 4)
print("\nAfter removing edge 3 -> 4:")
dg.display()
