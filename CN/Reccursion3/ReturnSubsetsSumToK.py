def SubsetsSumToK(lst,k):
    if len(lst) == 0:
        if k == 0:
            return [[]]
        return []

    #output including lst[0]
    op1 = SubsetsSumToK(lst[1:],k-lst[0])

    #output excluding lst[0]
    op2 = SubsetsSumToK(lst[1:],k)

    res = []
    for sub in op1:
        res.append([lst[0]]+sub)
    for row in op2:
        res.append(row)
    return res

print(SubsetsSumToK([5,12,3,17,1,18,15,3,17],6))