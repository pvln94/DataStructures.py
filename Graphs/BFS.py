# # AdjList
# from collections import deque

# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, u, v):
#         # Add an edge from node u to node v
#         if u in self.graph:
#             self.graph[u].append(v)
#         else:
#             self.graph[u] = [v]

#     def bfs(self, start):
#         visited = set()  # To keep track of visited nodes
#         queue = deque([start])  # Queue for BFS
        
#         while queue:
#             # Dequeue a node from the front of the queue
#             node = queue.popleft()
            
#             if node not in visited:
#                 print(node, end=" ")  # Process the current node
#                 visited.add(node)  # Mark the node as visited

#                 # Enqueue all unvisited adjacent nodes
#                 for neighbor in self.graph.get(node, []):
#                     if neighbor not in visited:
#                         queue.append(neighbor)

# # Example usage:
# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('B', 'E')
# g.add_edge('C', 'F')
# g.add_edge('C', 'G')
# g.add_edge('E', 'H')

# print("BFS traversal starting from node 'A':")
# g.bfs('A')



# AdjMatrix
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueuesLinked:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, item):
        temp = QueueNode(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.isempty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

class Graph:

    def __init__(self, vertices):
        self._adjMat = [[0] * vertices for _ in range(vertices)]
        self._vertices = vertices

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, '--', j)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if not self._adjMat[v][j] == 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for j in range(self._vertices):
            if not self._adjMat[j][v] == 0:
                count += 1
        return count

    def display_adjMat(self):
        for row in self._adjMat:
            print(row)

    def BFS(self, s):
        i = s
        q = QueuesLinked()
        visited = [0] * self._vertices
        print(i, end=' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.isempty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end=' ')
                    visited[j] = 1
                    q.enqueue(j)

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

print('Edges:')
G.edges()

print('BFS:')
G.BFS(0)
