class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLinkedList(head):
    while(head is not None):
        print(head.data,"->",end=" ")
        head = head.next
    print('None')

def takeInput(string):
    lst = list(map(int, string.split()))
    head = None

    for el in lst:
        if (el == -1):
            break
        newNode = Node(el)
        if head is None:
            head = newNode
            helper = head   #more efficient
        else:
            helper.next = newNode
            helper = newNode
    return head

def swap(head,n1, n2):
    ptr1 = head
    ptr2 = head
    i=0
    while i < n1:
        ptr1 = ptr1.next
        i+=1
    temp = ptr1.data
    i=0
    while i < n2:
        ptr2 = ptr2.next
        i+=1
    ptr1.data = ptr2.data
    ptr2.data = temp

    return head
    
l1 = takeInput("1 2 3 4 5 6 7 8 -1")
printLinkedList(l1)
swap(l1,0,4)
printLinkedList(l1)

    