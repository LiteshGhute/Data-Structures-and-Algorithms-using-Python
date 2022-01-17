import sys
def minimun(lst,res=sys.maxsize):
    if len(lst) == 0:
        print(res)
        return
    if lst[0] < res:
        res = lst[0]
    minimun(lst[1:],res)

minimun([2,3,4,5,1,7,8,9])