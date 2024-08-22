class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(map(str, self.graph[vertex]))}")

# Example usage
ug = UndirectedGraph()
ug.add_edge(1, 2)
ug.add_edge(1, 3)
ug.add_edge(2, 4)
ug.add_edge(3, 4)
ug.add_edge(4, 5)

print("\nUndirected Graph:")
ug.display()

# Removing an edge
ug.remove_edge(3, 4)
print("\nAfter removing edge 3 -- 4:")
ug.display()
