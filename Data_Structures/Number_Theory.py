from math import *
#Sum of n numbers with O(1)

def sum(n):
    return (n)*(n+1)//2 #O(1)
print(sum(122346556))

# GCD using euclid algo O(log(min(a,b)))

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
print(gcd(5,10))

# LCM using GCD

def lcm(a,b):
    prod = a*b
    hcf = gcd(a,b)
    return prod // hcf
print(lcm(20,50))

# Find number of divisors O(root(n))

def divisors(n):
    div=set()
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            div.add(i)
            div.add(n//i)
    return div
print(*divisors(24))


