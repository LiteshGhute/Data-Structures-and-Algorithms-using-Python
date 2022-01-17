import collections
import queue
#Double-Ended Queue
q=collections.deque()
q.append(10)
q.append(20)
q.append(30)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
print()
######################

q1= queue.Queue()   #using Queue calss
q1.put(10)
q1.put(50)
q1.put(30)
print(q1)
print(q1.get())
