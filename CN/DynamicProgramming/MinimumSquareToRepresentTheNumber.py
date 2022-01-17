import sys
def MinSq(n,dp):
    if n == 0:
        return 0
    
    ans = sys.maxsize
    i=1
    while(i*i<=n):
        if dp[n-i*i] == -1:
            smallAns = MinSq(n-i*i,dp)
            current_ans = 1 + smallAns
            dp[n-i*i] = smallAns
        else:
            current_ans = 1 + dp[n-i*i]
        ans = min(ans,current_ans)
        i+=1
    return ans
n=int(input())
dp = [-1]*(n+1)
print(MinSq(n,dp))