def fun(lst):
    l = len(lst)
    if l == 1 or l == 0:
        return True
    elif lst[0] > lst[1]:
        return False
    return fun(lst[1:])    #pass the entire list except 1st element
print(fun([1,2,3,4,4,6]))
print(fun([24,25,1,2,99]))