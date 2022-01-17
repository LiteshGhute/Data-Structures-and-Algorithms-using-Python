# A child is running up a staircase with N steps, and can hop either 1 step,
# 2 steps or 3 steps at a time. Calculate how many number of possible ways,
# a child can climb the staircase.

def StairCase(n):
    # Base Cases
    if n == 1:
        return 1    # There is only one way to climb 1 step at a time
    if n == 2:
        return 2    # There are 2 ways to climb 2 steps
    if n == 3:
        return 4    # There are 4 ways to climb 3 steps

    # If child climbs 1 step at a time then sum of remaining n-1 steps
    x = StairCase(n-1)
    # If child climbs 2 steps at a time then sum of remaining n-2 steps
    y = StairCase(n-2)
    # If child climbs 3 steps at a time then sum of remaining n-3 steps
    z = StairCase(n-3)

    return x+y+z    # Adding total sum and returning

print(StairCase(5))
print(StairCase(4))