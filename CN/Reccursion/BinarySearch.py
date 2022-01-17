def BinarySearch(a, x, si, ei):
    if si > ei:
        return -1
    mid = (si+ei)//2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return BinarySearch(a, x, si, mid-1)
    elif a[mid] < x:
        return BinarySearch(a, x, mid+1, ei)
print(BinarySearch([1,2,4,7,8,9,10,11,15],10, 0, 8))