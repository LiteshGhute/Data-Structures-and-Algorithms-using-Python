class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLinkedList(head):
    while(head is not None):
        print(head.data,"->",end=" ")
        head = head.next
    print('None')

def takeInput():
    lst = list(map(int, input().split()))
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

            # less efficient
            # curr = head
            # while curr.next is not None:
            #     curr = curr.next
            # curr.next = newNode

    return head

def insertReccursively(head, data, index):
    if index < 0:
        print('Invalid Index')
        return head
    if index == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    if head == None:
        return head

    smallHead = insertReccursively(head.next, data, index-1)
    head.next = smallHead
    return head

def reverse(head):
    if head.next == None:
        print(head.data,"->",end=" ")
        return
    reverse(head.next)
    print(head.data,"->",end=" ")


def insert(head, data, pos):
    count = 0
    storeHead = head
    
    if pos == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    while(count < pos-1 and head.next is not None):
        head = head.next
        count += 1
    if head.next is not None:
        newNode = Node(data)
        newNode.next = head.next
        head.next = newNode
        return storeHead
    elif  head.next is None and  count+1 == pos:
        newNode = Node(data)
        head.next = newNode
        return storeHead
    else:
        print('Invalid position')

def delete(head, index):
    storeHead = head
    if index == 0:
        return head.next
    count = 0
    while(head is not None):
        count += 1
        if count == index:
            head.next = head.next.next
            return storeHead
        head = head.next
    if count+1 == index:
        head.next = None
        return storeHead
    


head = takeInput()
printLinkedList(head)
newhead=insert(head, 10, 1)
printLinkedList(newhead)
dnode = delete(newhead,2)
printLinkedList(dnode)
pn = insertReccursively(dnode, 11, 1)
printLinkedList(pn)
reverse(pn)