def check(lst, n):
    l = len(lst)
    if l == 0:
        return False
    elif l == 1:
        if lst[0] == n:
            return True
        return False
    else:
        if(lst[0]==n):
            return True
        return check(lst[1:],n)
print(check([1,2,3,4],4))