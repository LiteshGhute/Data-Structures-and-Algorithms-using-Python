import sys,math
def minSq(n):
    dp = [-1] * (n+1)
    dp[0] = 0 #Base Case

    for i in range(1,n+1):  #represents reccursion loop
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1,root+1):   #actual loop for every n value
            currAns = 1 + dp[i-(j*j)]
            ans = min(ans,currAns)
        dp[i] = ans
    return dp[n]

print(minSq(int(input())))