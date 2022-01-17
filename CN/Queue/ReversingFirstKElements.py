import queue

def reverseFirstKElements(q, k):
    for _ in range(k):
        q.put(q.get())

    st1 = queue.LifoQueue()
    st2 = queue.LifoQueue()

    for _ in range(q.qsize()-k):
        st1.put(q.get())

    for _ in range(q.qsize()):
        st2.put(q.get())

    while not st2.empty():
        q.put(st2.get())

    while not st1.empty():
        st2.put(st1.get())

    while not st2.empty():
        q.put(st2.get())

    return q



q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
res=reverseFirstKElements(q, 3)

while not res.empty():
    print(res.get())