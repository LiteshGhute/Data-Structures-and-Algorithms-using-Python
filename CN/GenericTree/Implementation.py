import queue
class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = list()

def printTree(root):
    #Edge Case
    if root == None:
        return
    print(root.data)
    for child in root.children: #Base Case
        printTree(child)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()
    for child in root.children:
        printTreeDetailed(child)

def takeTreeInput():
    print('Enter root data')
    rootData =  int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    print('Enter no. of childer for ', rootData)
    childrenCount = int(input())
    for _ in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    
    return root


def numNodes(root):
    #Edge Case
    if root == None:
        return 0
    count = 1
    for child in root.children:     #Base Case
        count += numNodes(child)
    return count

def takeLevelWiseInput():
    q = queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)
    while(not q.empty()):
        currt_node = q.get()
        print('Enter num of children for ', currt_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print('Enter next child for ', currt_node.data)
            childData = int(input())
            child = TreeNode(childData)
            currt_node.children.append(child)
            q.put(child)

    return root


# n1 = TreeNode(5)
# n2 = TreeNode(2)
# n3 = TreeNode(9)
# n4 = TreeNode(8)
# n5 = TreeNode(7)
# n6 = TreeNode(15)
# n7 = TreeNode(1)

# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)

# n3.children.append(n6)
# n3.children.append(n7)

n1 = takeLevelWiseInput()

printTreeDetailed(n1)
print(numNodes(n1))