import queue
def stockSpan(lst):
    res = []
    st = queue.LifoQueue()
    st.put(0)
    res.append(1)
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            st.put(i+1)
            res.append(1)
        if lst[i] < lst[i+1]:
            while st.get() < lst[i+1]:
                if st.empty():
                    break
            st.put(i+1)
            res.append(i+2)
    return res

# lst = list(map(int, input().split()))
print(stockSpan([5,3,8,7,10,7,7,12,16]))