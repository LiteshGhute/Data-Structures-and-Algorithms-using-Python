import collections
import queue
stack=collections.deque()

stack.append(10)
stack.append(20)

print(stack)
stack.pop()
print(stack)

stack2 = queue.LifoQueue()
stack2.put(50)
stack2.put(100)

print(stack2.get())