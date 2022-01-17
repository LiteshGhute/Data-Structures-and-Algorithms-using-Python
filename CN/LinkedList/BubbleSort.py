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
   
def bubbleSort(head, n):
    storehead = head
    for _ in range(n):
        index = 0
        while head.next:
            if head.data > head.next.data:
                swap(storehead, index, index+1)
            head = head.next
            index+=1
        head = storehead
    return storehead


l1 = takeInput("2 4 1 3 6 5 -1")
printLinkedList(l1)
sl = bubbleSort(l1,6)
printLinkedList(sl)