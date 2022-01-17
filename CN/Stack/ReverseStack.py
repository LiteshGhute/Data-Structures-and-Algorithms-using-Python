import queue
def reverseStack(s1, s2):
    #if s1 has only one element left then return
    #Base Case
    if s1.qsize() == 1:
        return
    #move n-1 elements from s1 to s2
    for _ in range(s1.qsize()-1):
        s2.put(s1.get())
    #store the value of last element
    lastElement = s1.get()
    #move all elements from s2 to s1
    for _ in range(s2.qsize()):
        s1.put(s2.get())
    #reccursion
    reverseStack(s1,s2)
    #store nth element in s1
    s1.put(lastElement)


s1 = queue.LifoQueue()
s2 = queue.LifoQueue()
s1.put(40)
s1.put(30)
s1.put(20)
s1.put(10)
while not s1.empty():
    print(s1.get())
s1.put(40)
s1.put(30)
s1.put(20)
s1.put(10)
reverseStack(s1,s2)
while not s1.empty():
    print(s1.get())