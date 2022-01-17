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

graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print(graph)
add_edge('A','B')
add_edge('B','C')
add_edge('A','D')
print(graph)
delete_node('D')
print('After removing node "D"')
print(graph)
delete_edge('B','C')
print('After deleting edge b/w "B" and "C"')
print(graph)