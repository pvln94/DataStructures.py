class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1][vertex2] = 1
        self.graph[vertex2][vertex1] = 1

    def remove_edge(self, vertex1, vertex2):
        self.graph[vertex1][vertex2] = 0
        self.graph[vertex2][vertex1] = 0

    def display(self):
        for row in self.graph:
            print(" ".join(map(str, row)))

# Example usage
ug = UndirectedGraph(5)
ug.add_edge(0, 1)
ug.add_edge(0, 2)
ug.add_edge(1, 3)
ug.add_edge(2, 3)
ug.add_edge(3, 4)

print("\nUndirected Graph (Adjacency Matrix):")
ug.display()

# Removing an edge
ug.remove_edge(2, 3)
print("\nAfter removing edge 2 -- 3:")
ug.display()
