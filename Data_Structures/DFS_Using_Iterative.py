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

def DFS(node,graph):
    visited = set()
    if node not in graph:
        print("Node not present")
        return
    stack=[]
    stack.append(node)
    while stack:            #while stack is not empty
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            print(curr)
            for i in graph[curr]:
                stack.append(i)


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
DFS('B',graph)