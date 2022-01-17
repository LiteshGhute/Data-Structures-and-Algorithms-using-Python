def first_occurance(lst,n, i=0):    # i is counting number of passes
    l = len(lst)
    if l == 0:
        return -1
    elif l == 1 and lst[0] == n:
        return i
    else:
        if lst[0] == n:
            return i
    return first_occurance(lst[1:],n,i+1)
print(first_occurance([1,4,5,2],2))