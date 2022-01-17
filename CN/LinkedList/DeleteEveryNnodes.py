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

def deleteNnodes(head,n,m):
    ptr1 = head
    ptr2 = head
    t1=0
    t2=0
    c=1
    while True:
        while ptr1 and t1 < n:
            ptr2 = ptr2.next
            if ptr1 == head and n == 1 and c == 1:
                c += 1
                break
            if ptr1 == head and t1 == 0 and n != 1:
                t1 += 1
                continue

            ptr1 = ptr1.next
            t1 += 1
        t1=0
        while ptr2 and t2 < m:
            ptr2 = ptr2.next
            t2 += 1
        t2=0
        ptr1.next = ptr2

        if ptr2 is None or ptr1 is None:
            break
    return head

l1 = takeInput('1 2 3 4 5 6 7 8 -1')
printLinkedList(l1)
deleteNnodes(l1,2, 3)
printLinkedList(l1)