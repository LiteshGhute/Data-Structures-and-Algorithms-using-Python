import sys
def minCost(cost,i,j):
    num_rows = len(cost)
    num_cols = len(cost[0])

    #base cases
    if i >= num_rows or j >= num_cols:
        return sys.maxsize

    #special case
    if i == num_rows-1 and j == num_cols-1:
        return cost[i][j]

    ans1 = minCost(cost,i+1,j)
    ans2 = minCost(cost,i+1,j+1)
    ans3 = minCost(cost,i,j+1)

    smallOutput = min(ans1,ans2,ans3)
    finalOutput = cost[i][j] + smallOutput
    return finalOutput


cost = [[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
print(minCost(cost,0,0))