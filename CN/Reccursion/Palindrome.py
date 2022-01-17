def palindrome(a, si, ei):
    # Base Case
    if ei == 0:         # or we can write: if si >= ei: return True
        return True

    # Compare 1st and last element
    if a[si] == a[ei]:
        result = palindrome(a,si+1,ei-1)   # if 1st and last element is same then call reccursion on the remaining string
    else:
        result = False                     # if not same then its not a palindrome
    
    # Return result
    return result

print(palindrome('ababa',0,4))
print(palindrome('a',0,0))
print(palindrome('aa',0,1))
print(palindrome('ab',0,1))
print(palindrome('abb',0,2))
print(palindrome('abba',0,3))