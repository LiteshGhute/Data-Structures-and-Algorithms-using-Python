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

nodes=[]
graph=[]
node_count=0

print('Brfore adding nodes')
print(nodes)
print(graph)
add_node('A')
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print('After adding nodes')
print(nodes)
print(graph)
print_graph(graph)