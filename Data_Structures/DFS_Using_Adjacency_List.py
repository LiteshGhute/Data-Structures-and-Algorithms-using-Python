def add_node(node):
    if node in graph:
        print('node already present')
        return
    graph[node]=[]

def add_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print('one of node is not present')
        return
    graph[v1].append(v2)
    graph[v2].append(v1)

def delete_node(node):
    if node not in graph:
        print('Node not present')
        return
    graph.pop(node)
    for lst in graph.values():
        if node in lst:
            lst.remove(node)

def delete_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print('one of node is not present')
        return
    graph[v1].remove(v2)
    graph[v2].remove(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print('Node not present')
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
    

visited = set()
graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','B')
add_edge('B','D')
add_edge('A','D')
add_edge('A','C')
add_edge('C','D')
print(graph)
DFS('B',visited,graph)