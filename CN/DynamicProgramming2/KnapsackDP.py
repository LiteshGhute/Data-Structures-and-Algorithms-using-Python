def knapsack(W,wt,val):
    n= len(val)
    dp = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(n-1,-1,-1):
        w=0
        while(w<=W):
            if wt[i]<=w:
                ans1 = val[i] + dp[i+1][w-wt[i]]
                ans2 = dp[i+1][w]
                ans = max(ans1,ans2)
            else:
                ans = dp[i+1][w]
            
            dp[i][w] = ans
            w+=1
    return dp[0][W]
print(knapsack(50,[20,25,30],[200,300,100]))