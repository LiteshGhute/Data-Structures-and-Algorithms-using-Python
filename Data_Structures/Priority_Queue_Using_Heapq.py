import heapq
lst = [(1,'lg'),(4,'sia'),(3,'rea')]
heapq.heapify(lst)
print(lst)
for _ in range(len(lst)):
    print(heapq.heappop(lst))
