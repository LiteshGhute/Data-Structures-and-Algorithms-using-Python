def GeoSum(n):      # calculating sum of 1/2^0 + 1/2^1 + ...
    # Base Case
    if n == 0:
        return 1

    # Calculate sum of n-1 terms
    SubSum = GeoSum(n-1)

    # Add nth term and sum of n-1 terms 
    res = SubSum + 1/(2**n)

    # Returning the result
    return res 

print(GeoSum(1))