def solution(n):
    answer =[[0]*i for i in range(1,n+1)]
    num = 1
    dx = [0,1,-1]; dy = [1,0,-1]
    x,y = 0,0
    i = 0
    while num <= (n*(n+1))//2 :
        answer[y][x] = num
        nx = x+dx[i]; ny = y+dy[i]; num+=1
        if 0<=ny<n and 0<=nx<=ny and answer[ny][nx]==0 :
            x, y = nx, ny
        else:
            i = (i+1)%3
            y+=dy[i]; x+=dx[i]
    return sum(answer,[])

from collections import deque
import math
def solution2(n):
    answer = [0 for i in range(1, (n*(n+1))//2+1)]
    num = deque([i for i in range(1, (n*(n+1))//2+1)])

    turn = 0
    turnPoint = 0
    start = 0
    k = 0
    current = 0
    while k<=n:
        current = turnPoint + 4*turn
        turnPoint = current

        for i in range(2*turn+1, n-k+2*turn):
            if num:
                answer[current] = num.popleft()
                current += i
            else:
                break
        k+=1

        for i in range(n-k+1):
            if num:
                answer[current] = num.popleft()
                current += 1
            else:
                break
        k+=1
        current-=1

        for i in range(n-k):
            if num:
                current+=(-n+i+turn)
                answer[current] = num.popleft()
            else:
                break
        k+=1
        turn+=1

    return answer

n = 10
print(solution(n))