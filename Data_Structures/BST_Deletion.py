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

    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key)
        if self.rchild:
            self.rchild.inOrder()

    def delete(self,data,curr):
        if self.key is None:
            print("Tree is Empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Not found")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Not found")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key=temp.key
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
                    temp=None
                    return
                return temp

            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key=temp.key
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
                    temp=None
                    return
                self = None
                return temp 
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)

root=bst(None)
lst = [10,11]

for el in lst:
    root.insert(el)

root.inOrder()
print()
if count(root)>1:
    root.delete(10,root.key)
else:
    print('cant perform deletion')
root.inOrder()
