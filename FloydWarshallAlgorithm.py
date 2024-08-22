V = 3 # dimensions of graph matrix
INF = 99999

def Floydwarshall(graph):
    dist = graph

    print(dist)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    print(dist)            
    printsolution(dist) 

def printsolution(dist):
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ") # prints INF
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()

if __name__ == "__main__":
    Graph = [[0,4,15],[8,0,2],[3,INF,0]]     
    Floydwarshall(Graph)          
