class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start, end):
        self.graph[start][end] = 1

    def remove_edge(self, start, end):
        self.graph[start][end] = 0

    def display(self):
        for row in self.graph:
            print(" ".join(map(str, row)))

# Example usage
dg = DirectedGraph(5)
dg.add_edge(0, 1)
dg.add_edge(0, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 3)
dg.add_edge(3, 4)

print("Directed Graph (Adjacency Matrix):")
dg.display()

# Removing an edge
dg.remove_edge(2, 3)
print("\nAfter removing edge 2 -> 3:")
dg.display()
