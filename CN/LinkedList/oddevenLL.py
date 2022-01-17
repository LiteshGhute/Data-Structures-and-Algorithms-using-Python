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

def oddeven(head):              #segregate odd from even
    oddHead = Node(0)
    oddTail = oddHead
    evenHead = Node(0)
    evenTail = evenHead

    while head is not None:
        if head.data %2 != 0:
            oddTail.next = head
            head = head.next
            oddTail = oddTail.next
        if head.data %2 == 0:
            evenTail.next = head
            head = head.next
            evenTail = evenTail.next
    oddTail.next = None
    evenTail.next = None

    oddTail.next = evenHead.next

    return oddHead.next



l1 = takeInput('1 2 3 4 5 6 -1')
printLinkedList(l1)
oe = oddeven(l1)
printLinkedList(oe)