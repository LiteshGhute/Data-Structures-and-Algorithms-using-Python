class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n=n.nref
    def print_Reverse_DLL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n=n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head=new_node
        else:
            print("DLL is not empty")
    
    def insert_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,node):
        if self.head is None:
            print("DLL is empty")
        else:
            n=self.head
            while n is not None:
                if node == n.data:
                    break
                n=n.nref
            if n is None:
                print("Node not found")
                return
            new_node=Node(data)
            new_node.nref=n.nref
            new_node.pref=n
            if n.nref is not None:
                n.nref.pref=new_node
            n.nref=new_node

    def add_before(self,data,node):
        if self.head is None:
            print("DLL is empty")
        else:
            n=self.head
            while n is not None:
                if node == n.data:
                    break
                n=n.nref
            if n is None:
                print("Node not found")
                return
            new_node=Node(data)
            new_node.nref=n
            new_node.pref=n.pref
            if n.pref is not None:
                n.pref.nref=new_node
            else:
                self.head=new_node
            n.pref=new_node

    def delete_begin(self):
        if self.head is not None:
            if self.head.nref is not None:
                self.head=self.head.nref
                self.head.pref=None
                return
            self.head = None
        else:
            print("DLL is Empty")

    def delete_end(self):
        if self.head is None:
            print("DLL is empty")
        else:
            if self.head.nref is None:
                self.head=None
            else:
                n=self.head
                while n.nref is not None:
                    n=n.nref
                n.pref.nref = None
    
    def delete_Node(self,data):
        if self.head is None:
            print("DLL is empty")
        else:
            if self.head.nref is None:
                if self.head.data == data:
                    self.head=None
                else:
                    print("Node not present")
            else:
                n=self.head
                while n.nref is not None:
                    if n.data == data and n.nref is not None and n.pref is not None:
                        n.pref.nref=n.nref
                        n.nref.pref=n.pref
                        return
                    elif n.data == data and n.pref is None:
                        n.nref.pref=None
                        self.head=n.nref
                        return
                    n=n.nref
                if n.data == data and n.nref is None:
                        n.pref.nref=None
                        return
                print("Node not present")



dll1=DoublyLL()
dll1.insert_empty(40)
dll1.insert_begin(30)
dll1.insert_begin(20)
dll1.insert_begin(10)
dll1.insert_end(50)
dll1.add_after(60,50)
dll1.add_after(25,20)
dll1.add_before(1,10)
dll1.print_DLL()
print()
dll1.print_Reverse_DLL()
print()
dll1.delete_begin()
dll1.print_DLL()
print()
dll1.print_Reverse_DLL()
print()
dll1.delete_end()
dll1.print_DLL()
print()
dll1.print_Reverse_DLL()
print()
dll1.delete_Node(25)
dll1.print_DLL()
print()
dll1.print_Reverse_DLL()