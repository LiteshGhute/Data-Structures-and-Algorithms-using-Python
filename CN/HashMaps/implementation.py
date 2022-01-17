class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self) -> None:
        self.bucketSize = 10
        self.buckets = [None for value in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketSize))


    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2*self.bucketSize
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

    def insert(self, key, value):

        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()


    def search(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return "Key Not Found"


    def delete(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.buckets[index] = head.next
                    self.count -= 1
                    return head.value
                previous.next = head.next
                self.count -= 1
                return head.value
            previous = head
            head = head.next
        return None

m = Map()
m.insert('LG',1)
m.insert('DJ',"hi")
print(m.size())
m.delete('DJ')
print(m.size())
print(m.search('DJ'))
