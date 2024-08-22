import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def prim_mst(self):
#1
        result = []  # This will store the resultant MST
        adj_list = [[] for _ in range(self.V)]
#2
        for u, v, w in self.edges:
            adj_list[u].append((w, v, u))
            adj_list[v].append((w, u, v))
#3
        min_heap = [(0, 0, -1)]  # Priority queue with (weight, vertex, parent)
        in_mst = [False] * self.V  # MST inclusion list
#4
        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
#5            
            if in_mst[u]:
                continue
            else:
                in_mst[u] = True
#6
            if parent != -1:
                result.append([parent, u, weight])
#7
            for w, v, original_u in adj_list[u]:
                if not in_mst[v]:
                    heapq.heappush(min_heap, (w, v, u)) #type:ignore
        
        return result

# Driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

result = g.prim_mst()
print("Following are the edges in the constructed MST")
for edge in result:
    print(edge)