import queue
class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print('L',root.left.data,end=',')
    if root.right != None:
        print('R',root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def countNodes(root):
    if root is None:
        return 0

    leftCount = countNodes(root.left)
    rightCount = countNodes(root.right)

    return 1 + leftCount + rightCount

def LargestNode(root):
    if root is None:
        return -1
    lmax = LargestNode(root.left)
    rmax = LargestNode(root.right)
    return max(root.data,lmax,rmax)

def findHeight(root):
    if root is None:
        return 0

    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)
    return max(leftHeight,rightHeight)+1

def NumberofLeafNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    numberofLeafsOnLeft = NumberofLeafNodes(root.left)
    numberofLeafsOnRight = NumberofLeafNodes(root.right)
    return numberofLeafsOnLeft + numberofLeafsOnRight

def printAllNodesAtDepthK(root,k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printAllNodesAtDepthK(root.left,k-1)
    printAllNodesAtDepthK(root.right,k-1)

def NewPrintAllNodesAtDepthK(root, k, d=0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    NewPrintAllNodesAtDepthK(root.left,k,d+1)
    NewPrintAllNodesAtDepthK(root.right,k,d+1)

def isBalanced(root):
    if root == None:
        return True

    leftHeight = findHeight(root.left)
    rightHeight = findHeight(root.right)
    if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1:
        return False
    isleftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)

    if isleftBalanced and isRightBalanced:
        return True
    else:
        return False

def optimizedIsBalanced(root):
    if root == None:
        return 0, True

    lh, isLeftBalanced = optimizedIsBalanced(root.left)
    rh, isRightBalanced = optimizedIsBalanced(root.right)

    h = 1 + max(lh, rh)
    if lh - rh > 1 or rh -lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

def diameter(root):
    if root == None:
        return 0
    
    option1 = findHeight(root.left) + findHeight(root.right)
    option2 = diameter(root.left)
    option3 = diameter(root.right)
    return max(option1, option2, option3)


def takeLevelWiseInput():
    q=queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while(not q.empty()):
        current_node = q.get()
        print("Enter left child of ",current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter right child of ",current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root

def buildTreeFromPreIn(pre, inorder):
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(0,len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None
    
    leftInorder = inorder[0:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder+1:]

    lenLeftSubTree = len(leftInorder)

    leftPreorder = pre[1:lenLeftSubTree+1]
    rightPreoder = pre[lenLeftSubTree+1:]

    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreoder, rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root
        

# root = treeInput()
# root = takeLevelWiseInput()
root = buildTreeFromPreIn([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
printTreeDetailed(root)
print(optimizedIsBalanced(root))
