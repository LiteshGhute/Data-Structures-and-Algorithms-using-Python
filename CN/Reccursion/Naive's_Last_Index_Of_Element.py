def last_index_of(lst, n):
    l = len(lst)
    if l == 0:
        return -1
    smaller_list_output = last_index_of(lst[1:],n)
    if smaller_list_output != -1:
        return smaller_list_output + 1
    else:
        if lst[0] == n:
            return 0
        return -1
print(last_index_of([1,2,3,4,5,6,4,8],4))