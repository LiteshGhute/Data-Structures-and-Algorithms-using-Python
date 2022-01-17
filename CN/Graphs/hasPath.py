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

    def hasPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__helperhasPath(visited, v1, v2)
    
    def __helperhasPath(self,visited, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True        
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                query = self.__helperhasPath(visited,i,v2)
                if query:
                    return True
                return False
        return False


g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.hasPath(3,1))