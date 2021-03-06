def merge(a1, a2, a):
    i=0
    j=0
    k=0
    while i < len(a1) and j < len(a2):
        if a1[i] <a2[j]:
            a[k] = a1[i]
            k+=1
            i+=1
        else:
            a[k]=a2[j]
            k+=1
            j+=1
    while i < len(a1):  #to append remaining elements if it's in a1
        a[k] = a1[i]
        k+=1
        i+=1
    while j < len(a2):  #to append remaining elements if it's in a2
        a[k] = a2[j]
        k+=1
        j+=1

def mergeSort(a):
    l = len(a)
    if l == 0 or l == 1:
        return
    mid = l//2
    a1 = a[0:mid]
    a2 = a[mid:]
    mergeSort(a1)    #hypothesis: we will get sorted array
    mergeSort(a2)    #hypothesis: we will get sorted array
    merge(a1,a2,a)            #merging two sorted array

lst=[2,3,4,5,7,1,7]
mergeSort(lst)
print(lst)