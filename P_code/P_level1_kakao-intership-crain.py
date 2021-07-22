board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

newboard = []
for i in range(0, len(board)):
    temp = []
    for j in range(0, len(board)):
        if(board[j][i]!=0):
            temp.append(board[j][i])
    newboard.append(temp)

basket = []
answer = 0

for m in range(0, len(moves)):
    moving = moves[m]-1
    for i in range(0, len(board)):
        if(board[i][moving] != 0):
            basket.append(board[i][moving])
            board[i][moving] = 0
            break
    if(len(basket)>1):
        if(basket[-1]==basket[-2]):
            del basket[-1]
            del basket[-1]
            answer+=2

