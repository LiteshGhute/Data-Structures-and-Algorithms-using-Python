def printPathHelper(x,y,maze,n,solution):
    #reached to the end
    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return
    #base cases (blocking points)
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y]==0 or solution[x][y]==1:
        return

    #if we reached here that means solution is present
    solution[x][y]=1
    printPathHelper(x+1,y,maze,n,solution)
    printPathHelper(x,y+1,maze,n,solution)
    printPathHelper(x,y-1,maze,n,solution)
    printPathHelper(x-1,y,maze,n,solution)
    solution[x][y] = 0  #after printing current path make it 0 to print other present paths from that route
    return

def printPath(maze):
    n = len(maze)
    solution = [[0 for j in range(n)]for i in range(n)]
    printPathHelper(0,0,maze,n,solution)

n = int(input())
maze = []
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)
printPath(maze)