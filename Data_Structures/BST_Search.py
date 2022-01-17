class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key == data:    #to ignore duplicate key
            return
        if self.key > data:
            if self.lchild:     #if left child is present
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)
        else:
            if self.rchild:     #if right child is present
                self.rchild.insert(data)
            else:
                self.rchild=bst(data)

    def search(self,data):
        if self.key == data:
            print("Node found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node not found")
    

root=bst(None)
lst = [5,11,2,1,3,12,15,30]

for el in lst:
    root.insert(el)

root.search(5)
root.search(10)