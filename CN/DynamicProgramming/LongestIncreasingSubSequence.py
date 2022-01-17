def LIS(lst,i,n,dp):
    if i == n:
        return 0, 0

    including_max = 1
    for j in range(i+1,n):
        if lst[j] >= lst[i]:
            if dp[j] == -1:
                ans = LIS(lst,j,n,dp)
                dp[j] = ans
                further_including_max = ans[0]
            else:
                further_including_max = dp[j][0]
            including_max = max(including_max, 1+ further_including_max)
    if dp[i+1] == -1:
        ans = LIS(lst,i+1,n,dp)[1]
        dp[i+1] = ans
        excluding_max = ans
    else:
        excluding_max = dp[i+1][1]
    overallMax = max(including_max,excluding_max)
    return including_max,overallMax

n = int(input())
lst = [int(ele) for ele in input().split()]
dp = [-1] * (n+1)
ans = LIS(lst,0,n,dp)[1]
print(ans)