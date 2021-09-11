import copy
def winnerA(board, aloc, bloc):
    answer = 0
    row, col = len(board), len(board[0])
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 오른쪽 왼쪽 아래쪽 위쪽
    while True:
        mini = (row ** 2) * (col ** 2) + 1
        minInd = -1
        for i in range(4):
            ny = aloc[0] + dr[i][0]
            nx = aloc[1] + dr[i][1]
            if (0 <= nx and nx < col) and (0 <= ny and ny < row) and board[ny][nx] != 0:
                distance = (ny - bloc[0]) ** 2 + (nx - bloc[1]) ** 2
                if distance <= mini:
                    mini = distance
                    minInd = i
        # 이동할 방향이 없는 경우
        if minInd == -1:
            break
        else:
            board[aloc[0]][aloc[1]] = 0
            aloc[0], aloc[1] = aloc[0] + dr[minInd][0], aloc[1] + dr[minInd][1]
            answer += 1
            if board[bloc[0]][bloc[1]] == 0:
                break

        maxi = 0
        maxInd = -1
        for i in range(4):
            ny = bloc[0] + dr[i][0]
            nx = bloc[1] + dr[i][1]
            if (0 <= nx and nx < col) and (0 <= ny and ny < row) and board[ny][nx] != 0:
                distance = (ny - aloc[0]) ** 2 + (nx - aloc[1]) ** 2
                if distance >= maxi:
                    maxi = distance
                    maxInd = i
        if maxInd == -1:
            break
        else:
            board[bloc[0]][bloc[1]] = 0
            bloc[0], bloc[1] = bloc[0] + dr[maxInd][0], bloc[1] + dr[maxInd][1]
            answer += 1
            if board[aloc[0]][aloc[1]] == 0:
                break
    return answer

def winnerB(board, aloc, bloc):
    answer = 0
    row, col = len(board), len(board[0])
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 오른쪽 왼쪽 아래쪽 위쪽
    while True:
        maxi = 0
        maxInd = -1
        for i in range(4):
            ny = aloc[0] + dr[i][0]
            nx = aloc[1] + dr[i][1]
            if (0 <= nx and nx < col) and (0 <= ny and ny < row) and board[ny][nx] != 0:
                distance = (ny - bloc[0]) ** 2 + (nx - bloc[1]) ** 2
                if distance>=maxi:
                    maxi = distance
                    maxInd = i
        if maxInd == -1:
            break
        else:
            board[aloc[0]][aloc[1]] = 0
            aloc[0], aloc[1] = aloc[0] + dr[maxInd][0], aloc[1] + dr[maxInd][1]
            answer += 1
            if board[bloc[0]][bloc[1]] == 0:
                break

        mini = (row ** 2) * (col ** 2) + 1
        minInd = -1
        for i in range(4):
            ny = bloc[0] + dr[i][0]
            nx = bloc[1] + dr[i][1]
            if (0 <= nx and nx < col) and (0 <= ny and ny < row) and board[ny][nx] != 0:
                distance = (ny - aloc[0]) ** 2 + (nx - aloc[1]) ** 2
                if distance <= mini:
                    mini = distance
                    minInd = i
        # 이동할 방향이 없는 경우
        if minInd == -1:
            break
        else:
            board[bloc[0]][bloc[1]] = 0
            bloc[0], bloc[1] = bloc[0] + dr[minInd][0], bloc[1] + dr[minInd][1]
            answer += 1
            if board[aloc[0]][aloc[1]] == 0:
                break
    return answer

def solution(board, aloc, bloc):
    A = winnerA(copy.deepcopy(board),aloc.copy(),bloc.copy())
    B = winnerB(copy.deepcopy(board),aloc.copy(),bloc.copy())
    return min(A,B)

board = [[1, 1, 1, 1, 1]]
aloc = [0,0]
bloc = [0,4]
print(solution(board,aloc,bloc))