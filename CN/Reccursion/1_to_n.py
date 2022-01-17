def one_to_n(n):
    if n == 0:
        return
    one_to_n(n-1)
    print(n)
one_to_n(10)