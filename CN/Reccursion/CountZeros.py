def countZeros(n):
    # Base cases:
    
    # 1) If no. is 0 itself then return 1
    if n == 0:
        return 1
    # 2) If no. is single digit no. but not equal to 0 then return 0
    if n < 10:
        return 0

    # Reccursion step
    else:
        if n % 10 == 0:                 # Checking last digit is 0 or not
            res = 1 + countZeros(n//10) # If its 0 then add 1 to count of n-1 terms
            return res
        else:
            res = 0 + countZeros(n//10) # if its not 0 then return count of n-1 terms
            return res

print(countZeros(10001))
