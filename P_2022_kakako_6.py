def solution2(board, skill):
    answer = 0
    for i in range(len(board)):#0~3행
        for j in range(len(board[i])): #0~4 열
            for sk in skill:
                if (sk[1]<=i and i<=sk[3]) and (sk[2]<=j and j<=sk[4]):
                    if sk[0] == 1:
                        board[i][j] -= sk[5]
                    else:
                        board[i][j] += sk[5]
            if board[i][j]> 0:
                answer+=1
    return answer

def solution(board, skill):
    answer =0

    return answer
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))