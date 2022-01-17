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
    
    def __helpergetPath(self,visited, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return [v2]
                   
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                query = self.__helpergetPath(visited,i,v2)
                if query:
                    query.append(i)
                    return query
        return None

    def getPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        res = self.__helpergetPath(visited, v1, v2)
        res.append(v1)
        return res


g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 4)
g.addEdge(3, 5)
g.addEdge(5, 6)
print(g.getPath(1, 6))