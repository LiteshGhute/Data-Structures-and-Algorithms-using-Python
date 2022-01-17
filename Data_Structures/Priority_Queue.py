import queue
q=[]
q.append(10)
q.append(40)
q.append(20)
q.sort()    #lower the value higher the priority
print(q)
q.pop(0)
print(q)
q.pop(0)
print(q)
print()
##################################################
que = queue.PriorityQueue()
que.put(10)
que.put(30)
que.put(60)
que.put(20)
que.put(40)

print(que.get())
print(que.get())