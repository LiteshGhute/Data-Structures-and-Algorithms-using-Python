import heapq

heap=[]
heapq.heappush(heap,10) #min heap
heapq.heappush(heap,1)
heapq.heappush(heap,5)
print(heap)

print(heapq.heappop(heap))
print(heap)


lst = [5,6,1,2,8,7,3]
heapq.heapify(lst)
print(lst)
print(heapq.heappushpop(lst,89))
print(lst)

print(heapq.heapreplace(lst,100))
print(lst)

print(heapq.nsmallest(2,lst))
print(heapq.nlargest(2,lst))