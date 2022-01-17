import queue

def isBalanced(expression):
    st = queue.LifoQueue()
    
    for el in expression:
        if el not in [')',']','}']:
            st.put(el)
        if el in [')',']','}']:
            count = 0
            while st.get() not in ['(','{','[']:
                count += 1
            if count == 0:
                return True
            else:
                continue
    if count != 0:
        return False
            


expression = input().split()
print(isBalanced(expression))