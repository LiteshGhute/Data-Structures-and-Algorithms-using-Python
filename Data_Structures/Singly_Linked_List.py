class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n=n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after(self, data, x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            else:
                n=n.ref
        if n is None:
            print("node is not present")
        else:
            new_node=Node(data)
            new_node.ref = n.ref
            n.ref=new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
            return
        n=self.head
        if n.data == x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        else:
            while n is not None:
                if n.ref.data==x:
                    break
                else:
                    n=n.ref
            if n is None:
                print("node is not present")
            else:
                new_node=Node(data)
                new_node.ref = n.ref
                n.ref=new_node
            
    def insert_empty(self,data):                #to insert a node in empty LL
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    def delete_begin(self):
        if self.head is None:
            print("Linked list is already empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref = None

    def delete_node(self,data):
        if self.head is None:
            print("Linked list is empty")
        else:
            if self.head.data == data:
                self.head = self.head.ref
            else:
                n=self.head
                while n.ref is not None:
                    if n.ref.data == data:
                        n.ref = n.ref.ref
                        return
                    n=n.ref
                print("data not present")





LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_begin(20)
LL1.print_LL()
LL1.add_after(200,10)
print()
LL1.print_LL()
print()
LL1.add_before(150,200)
LL1.print_LL()
print()
LL1.delete_begin()
LL1.print_LL()
print()
LL1.delete_end()
LL1.print_LL()
print()
LL1.delete_node(150)
LL1.print_LL()