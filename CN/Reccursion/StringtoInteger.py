def StringtoInt(a):     # Without using pre-defined int() function
    # Base Case
    if len(a) == 1:
        return ord(a) - 48  # Converting char into int

    # Getting the output of n-1 terms and appending nth term 
    num = StringtoInt(a[:-1]) * 10 + (ord(a[-1])-48)

    return num

integer = StringtoInt('1001')
print(type(integer))    # checking type