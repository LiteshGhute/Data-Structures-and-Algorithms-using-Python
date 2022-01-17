def LCS(str1,str2,i,j,dp):
    if len(str1) == i or len(str2) == j:
        return 0

    #if 1st char of both strings are equal
    if str1[i] == str2[j]:
        if dp[i+1][j+1] == -1:
            small_op = LCS(str1,str2,i+1,j+1,dp)
            dp[i+1][j+1] =  small_op
        else:
            small_op = dp[i+1][j+1]
        op = 1 +small_op

    #if not equal then
    if str1[i] != str2[j]:
        if dp[i+1][j] == -1:
            ans1 = LCS(str1,str2,i+1,j,dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]
        
        if dp[i][j+1] == -1:
            ans2 = LCS(str1,str2,i,j+1,dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]

        op = max(ans1,ans2)
    return op


dp=[[-1 for i in range(8)] for j in range(7)]
print(LCS("bedgmc","abdfglc",0,0,dp))