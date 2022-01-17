def last_index(lst, n, start_index=0):
    if len(lst) == start_index:
        return -1
    shorter_list_answer = last_index(lst, n, start_index+1)
    if shorter_list_answer != -1:
        return shorter_list_answer
    else:
        if lst[start_index] == n:
            return start_index
        return -1
print(last_index([1,2,3,4,5,6,4,8],4))