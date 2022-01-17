def fib(n):
    res = [0 for i in range(n+1)]
    res[0],res[1]=0,1
    if n == 0 or n == 1:
        return n
    for i in range(2,n+1):
        res[i] = res[i-1]+res[i-2]
    return res[n]

print(fib(7))