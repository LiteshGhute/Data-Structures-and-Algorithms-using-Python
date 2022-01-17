def isSafe(row,col,board,n):
    #check vertical direction
    i=row-1
    while i>=0:
        if board[i][col] == 1:
            return False
        i -= 1
    #check left upper diagonal
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    #check right upper diagonal
    i=row-1
    j=col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True
    
def printPathsHelper(row,n,board):
    #base case: if we reached to the last row then we got the solution
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end="")
        print()
        return
    
    for col in range(n):
        if isSafe(row,col,board,n):
            board[row][col] = 1
            printPathsHelper(row+1,n,board)
            board[row][col] = 0
    return

def printPaths(n):
    board = [[0 for i in range(n)] for j in range(n)]
    printPathsHelper(0,n,board)

n = int(input())
printPaths(n)