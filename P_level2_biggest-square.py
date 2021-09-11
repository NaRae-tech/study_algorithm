def check(row, column, n, board):
    for i in range(row, row+n):
        for j in range(column, column+n):
            if board[i][j]==0:
                return False
    return True
def solution(board):
   n = len(board)
   while n>0:
        for i in range(0,len(board)-n+1):
            for j in range(0,len(board[0])-n+1):
                if check(i,j,n,board):
                    return n**2
        n-=1
   return -1
board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))