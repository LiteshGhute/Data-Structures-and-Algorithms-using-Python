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

    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key)
        if self.rchild:
            self.rchild.inOrder()

    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key)

    def levelOrder(self):
        q = [self]  #checking root exists or not and then inserting 
        
        for current in q:
            if current:     #if current is not None then print data
                print(current.key, end=' ')

                q.append(current.lchild)  #appending left child to q
                q.append(current.rchild) #appending right child to q
        
        
        

root=bst(None)
lst = [5,11,2,1,3,12,15,30]

for el in lst:
    root.insert(el)

root.levelOrder()