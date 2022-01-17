def first_occurance(lst,n,start_index):
    l = len(lst)
    if l == start_index:
        return -1
    elif l == 1 and lst[0] == n:
        return 0
    else:
        if(lst[start_index] == n):
            return start_index
        return first_occurance(lst,n,start_index+1)
print(first_occurance([2,1,4],1,0))