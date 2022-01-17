class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self) -> None:
        self.__front = None
        self.__head = None
        self.__count = 0

    def enqueue(self, data):
        newNode = Node(data)
        
        if self.__count == 0:
            self.__front = newNode
            self.__head = newNode
            self.__count += 1
        
        else:
            self.__head.next = newNode
            self.__head = self.__head.next
            self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            return -1
        self.__front = self.__front.next
        self.__count -= 1

    def front(self):
        if self.__count == 0:
            return -1
        return self.__front.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.size())
while not q.isEmpty():
    print(q.front())
    q.dequeue()
