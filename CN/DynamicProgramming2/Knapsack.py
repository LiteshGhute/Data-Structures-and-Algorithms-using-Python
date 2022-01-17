def knapsack(w,wt,val,i=0):
    if i == len(wt):
        return 0
    
    #if weight of i'th item is greater than allowed weight
    if wt[i] > w:
        ans = knapsack(w,wt,val,i+1)
    
    else:
        # includuing ith element
        ans1 = val[i] + knapsack(w-wt[i],wt,val,i+1)
        # excluding ith element
        ans2 = knapsack(w,wt,val,i+1)

        ans = max(ans1, ans2)
    
    return ans

print(knapsack(500,[100,200,300],[800,200,100]))