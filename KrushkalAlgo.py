class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set

    def get_weight(self, edge):
        return edge[2]

    def kruskal_mst(self):
        result = []  # This will store the resultant MST

        # Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=self.get_weight)

        # Create a parent[] array to store the parent of each vertex
        parent = list(range(self.V))
        #print(parent)
        # Iterate over all edges
        for edge in self.graph:
            # Find the parent of each vertex
            u_parent = self.find(parent, edge[0])
            v_parent = self.find(parent, edge[1])

            # If the vertices do not belong to the same set, then include this edge in the MST
            if u_parent != v_parent:
                result.append(edge)
                self.union(parent, u_parent, v_parent)

        return result

# Driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
result = g.kruskal_mst()

print("Following are the edges in the constructed MST")
for edge in result:
    print(edge)