def PrintFactorial(n,res=1):
    if n == 0:
        print(res)
        return
    res = res * n
    PrintFactorial(n-1,res)

PrintFactorial(5)