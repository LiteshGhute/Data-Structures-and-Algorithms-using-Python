def sum_of_List(lst):
    l = len(lst)
    if l == 0:
        return 0
    elif l == 1:
        return lst[0]
    else:
        return lst[0]+sum_of_List(lst[1:])
print(sum_of_List([1,2,3,4,5]))