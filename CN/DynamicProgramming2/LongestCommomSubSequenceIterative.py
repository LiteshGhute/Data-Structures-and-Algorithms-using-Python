def LCS(str1, str2):
    dp=[[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

    for i in range(len(str1)-1,-1,-1):
        for j in range(len(str2)-1,-1,-1):

            if str1[i] == str2[j]:
                ans = 1 + dp[i+1][j+1]
            else:
                ans1 = dp[i][j+1]
                ans2 = dp[i+1][j]
                ans = max(ans1,ans2)
            dp[i][j] = ans

    return dp[0][0]
print(LCS("bedgmc","abdfglc"))