def solution(m,n,board):
    answer = 0
    table = []
    for i in range(m):
        table.append(list(board[i]))

    while True:
        check = [[False for i in range(n)] for j in range(m)]
        flag = False
        for i in range(m-1):
            for j in range(n-1):
                if (table[i][j]!=' ' and table[i][j]==table[i][j+1]  and table[i][j]==table[i+1][j] and table[i][j]==table[i+1][j+1]):
                    flag = True
                    if check[i][j] == False:
                        check[i][j]=True
                        answer+=1
                    if check[i][j+1] == False:
                        check[i][j+1] = True
                        answer += 1
                    if check[i+1][j] == False:
                        check[i+1][j] = True
                        answer += 1
                    if check[i+1][j+1] == False:
                        check[i+1][j+1] = True
                        answer += 1

        if flag != True:
            break
        else:
            for i in range(m):
                for j in range(n):
                    if check[i][j] == True:
                        table[i][j] =" "
            for i in range(m-1,-1,-1):
                for j in range(n):
                    if table[i][j]==" ":
                        for k in range(i-1,-1,-1):
                            if table[k][j] !=" ":
                                table[i][j] = table[k][j]
                                table[k][j] = " "
                                break
    return answer

m = 7
n = 2
board = ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]
print(solution(m,n,board))