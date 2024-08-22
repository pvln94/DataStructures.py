# # AdjList
# class Graph:

#     def __init__(self, vertices):
#         self._adjList = [[] for _ in range(vertices)]
#         self._vertices = vertices

#     def insert_edge(self, u, v):
#         self._adjList[u].append(v)

#     def DFS(self, s):
#         visited = [False] * self._vertices
#         self._DFS_util(s, visited)

#     def _DFS_util(self, v, visited):
#         visited[v] = True
#         print(v, end=' ')

#         for neighbor in self._adjList[v]:
#             if not visited[neighbor]:
#                 self._DFS_util(neighbor, visited)

# # Example usage:
# G = Graph(7)
# G.insert_edge(0, 1)
# G.insert_edge(0, 5)
# G.insert_edge(0, 6)
# G.insert_edge(1, 0)
# G.insert_edge(1, 2)
# G.insert_edge(1, 5)
# G.insert_edge(1, 6)
# G.insert_edge(2, 3)
# G.insert_edge(2, 4)
# G.insert_edge(2, 6)
# G.insert_edge(3, 4)
# G.insert_edge(4, 2)
# G.insert_edge(4, 5)
# G.insert_edge(5, 2)
# G.insert_edge(5, 3)
# G.insert_edge(6, 3)

# print('DFS:')
# G.DFS(0)


#AdjMat
class Graph:

    def __init__(self, vertices):
        self._adjMat = [[0] * vertices for _ in range(vertices)]
        self._vertices = vertices

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x

    def DFS(self, s):
        visited = [False] * self._vertices
        self._DFS_util(s, visited)

    def _DFS_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in range(self._vertices):
            if self._adjMat[v][i] == 1 and not visited[i]:
                self._DFS_util(i, visited)

# Example usage:
G = Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)

print('DFS:')
G.DFS(0)
