import sys
def minCostI(cost):
    m = len(cost)
    n = len(cost[0])
    dp = [[sys.maxsize for i in range(n+1)] for j in range(m+1)]

    for i in reversed(range(0,m)):
        for j in reversed(range(0,n)):
            if i==m-1 and j==n-1:
                dp[i][j] = cost[i][j]
                continue
            ans1 = dp[i][j+1]
            ans2 = dp[i+1][j]
            ans3 = dp[i+1][j+1]
            dp[i][j] = cost[i][j] + min(ans1,ans2,ans3)
    return dp[0][0]

cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
print(minCostI(cost))