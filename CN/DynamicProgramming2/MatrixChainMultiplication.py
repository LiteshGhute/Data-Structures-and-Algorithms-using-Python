import sys
def mcm(p,i,j,dp):
    if i == j:
        return 0

    min_value = sys.maxsize
    for k in range(i,j):
        if dp[i][k] == -1:
            ans1 = mcm(p,i,k,dp)
        else:
            ans1 = dp[i][k]

        if dp[k+1][j] == -1:
            ans2 = mcm(p,k+1,j,dp)
        else:
            ans2 = dp[k+1][j]

        mCost = p[i-1]*p[k]*p[j]
        curr_value = ans1 + ans2 + mCost
        min_value = min(min_value,curr_value)

    return min_value


p = [2,3,4,5,6]
n=len(p)-1
dp = [[-1 for i in range(n+1)] for j in range(n+1)]
print(mcm(p,1,n,dp))