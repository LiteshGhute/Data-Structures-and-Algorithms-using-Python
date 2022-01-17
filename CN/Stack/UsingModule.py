import queue

#inbuilt queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
    print(q.get())


#inbuilt stack
s = queue.LifoQueue()
s.put(1)
s.put(2)
s.put(3)
s.put(4)

while not s.empty():
    print(s.get())