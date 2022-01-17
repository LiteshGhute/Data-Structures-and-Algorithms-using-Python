def mul(n,m):
    # Base Case
    if m == 0:
        return 0

    # Reccursion call: adding nth term to the sum of n-1 terms
    result = n + mul(n,m-1)

    # Returning result
    return result

print(mul(2,8))