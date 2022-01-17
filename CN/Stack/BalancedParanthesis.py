import queue

def isBalanced(expression):
    st = queue.LifoQueue()
    # for el in expression:
    #     if el in ['{', '[', '(']:
    #         st.put(el)
    count = 0
    for el in expression:
        count += 1
        if el in ['{', '[', '(']:
            st.put(el)
        if el in ['}', ']', ')']:
            if st.empty():
                return False
            bracket = st.get()
            if bracket == '{' and el == '}':
                continue
            elif bracket == '[' and el == ']':
                continue
            elif bracket == '(' and el == ')':
                continue
            else:
                return False
        
    if count == len(expression) and st.empty():
        return True
    else:
        return False



expression = input().split()
print(isBalanced(expression))