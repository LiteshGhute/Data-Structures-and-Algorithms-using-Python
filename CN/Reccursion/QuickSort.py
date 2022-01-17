def partition(a, si, ei):
    #Select pivot
    p = a[si]

    #Now move pivot element to its correct location
    counter = 0
    for i in range(si,ei+1):
        if a[i] < p:
            counter += 1
    a[si+counter], a[si] = a[si], a[si+counter] #Swaping them
    pivot_index = si+counter

    #Now sort array around pivot
    i=si
    j=ei
    while i<j:
        if a[i] < p:
            i+=1
        elif a[j] >= p:
            j-=1
        else:           #When both the elements are at wrong place i.e., i and j both are at wrong place then swap them
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
    
    return pivot_index  #Return index of pivot element

def QuickSort(a, si, ei):
    #Base case
    if si >= ei:
        return
    
    #Get index around which partition is done
    i = partition(a, si, ei)

    #Call QuickSort function on the left and right of i
    QuickSort(a,si,i-1)
    QuickSort(a,i+1,ei)

lst=[5,4,3,2,1,7,9,5,6,10,8]
QuickSort(lst,0,10)
print(lst)