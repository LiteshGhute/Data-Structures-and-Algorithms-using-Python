class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEgde(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self) -> str:
        return str(self.adjMatrix)

    def __dfsHelper(self, startingVertex, visited):
        visited[startingVertex] = True
        for i in range(self.nVertices):
            if self.adjMatrix[startingVertex][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)
    
    def __Helperdfs2(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0, visited)
        return visited

    def isConnected(self):
        visited = self.__Helperdfs2()
        if False in visited:
            return False
        return True

g = Graph(7)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(4,6)
print(g.isConnected())

g2 = Graph(4)
g2.addEdge(0,1)
g2.addEdge(0,3)
g2.addEdge(1,2)
g2.addEdge(2,3)
print(g2.isConnected())