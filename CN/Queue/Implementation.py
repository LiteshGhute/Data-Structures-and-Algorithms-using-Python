class queue:
    def __init__(self) -> None:
        self.__array = []
        self.__count = 0
        self.__front = 0

    def enqueqe(self, data):
        self.__array.append(data)
        self.__count += 1
    
    def dequeqe(self):
        if self.__count == 0:
            return -1
        element = self.__array[self.__front]
        self.__count -= 1
        self.__front += 1
        return element

    def front(self):
        if self.__count == 0:
            return -1
        return self.__array[self.__front]

    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size() == 0

q = queue()
q.enqueqe(1)
q.enqueqe(2)
q.enqueqe(3)
q.enqueqe(4)
while q.isEmpty() is False:
    print(q.front())
    q.dequeqe()

print(q.size())
print(q.isEmpty())
    