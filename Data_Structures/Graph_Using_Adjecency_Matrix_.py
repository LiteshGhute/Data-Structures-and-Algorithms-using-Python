def add_node(node):
    global node_count
    if node in nodes:
        print("Node is already present")
        return
    node_count+=1
    nodes.append(node)
    for n in graph:
        n.append(0)
    graph.append([0 for _ in range(node_count)])

def print_graph(graph):
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=' ')
        print()

def add_edge(v1,v2):
    if v1 not in nodes or v2 not in nodes:
        print("one of the node not present")
        return
    graph[nodes.index(v1)][nodes.index(v2)]=1
    graph[nodes.index(v2)][nodes.index(v1)]=1
    return

def delete_node(node):
    global node_count
    if node not in nodes:
        print('Node not present')
        return
    ind=nodes.index(node)
    del nodes[ind]
    node_count-=1
    graph.pop(ind)  #removes row
    for i in graph: #to remove column
        i.pop(ind)

def delete_Edge(v1,v2):
    if v1 not in nodes or v2 not in nodes:
        print("one of the node not present")
        return
    graph[nodes.index(v1)][nodes.index(v2)]=0
    graph[nodes.index(v2)][nodes.index(v1)]=0
    return

nodes=[]
graph=[]
node_count=0

add_node('A')
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print('After adding nodes')
print(graph)
print_graph(graph)
print()
add_edge('A','B')
add_edge('B','C')
print_graph(graph)
delete_node('D')
print(nodes)
print_graph(graph)
delete_Edge('B','C')
print("Deleting edge b/w 'B' and 'C'")
print_graph(graph)