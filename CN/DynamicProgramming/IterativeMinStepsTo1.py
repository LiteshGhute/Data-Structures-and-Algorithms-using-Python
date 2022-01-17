n = int(input())

def getMinStepsTo1(n):
    memo = [-1] * (n+1)
    memo[1] = 0
   
    for i in range(2,n+1):
        curr_min = memo[i-1]
        if i%3==0:
            curr_min = min(curr_min,memo[i//3])
        if i%2==0:
            curr_min = min(curr_min,memo[i//2])
        memo[i] = 1 + curr_min
    return memo[n]
print(getMinStepsTo1(n))