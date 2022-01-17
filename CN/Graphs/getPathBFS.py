import queue
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

    def __getPathHelper(self, v1, v2, visited):
        res=[]
        q = queue.Queue()
        q.put(v1)
        visited[v1] = True
        dictionary = {}
        while q.empty() is False:
            front = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[front][i] > 0 and visited[i] is False:
                    dictionary[i] = front
                    q.put(i)
                    visited[i] = True
        key = v2
        while(key != v1):
            res.append(key)
            key = dictionary[key]
        res.append(v1)
        return res[::-1]

    def getPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathHelper(v1, v2, visited)
g = Graph(7)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(0,2)
g.addEdge(2,4)
g.addEdge(4,6)
g.addEdge(3,6)
print(g.getPath(1,6))