def turn_left():
    global direct
    direct-=1
    if(direct==-1):
        direct = 3
import sys
N,M = map(int, sys.stdin.readline().split())
x,y,direct = map(int, sys.stdin.readline().split())
gameMap = []
for _ in range(N):
    gameMap.append(list(map(int,sys.stdin.readline().split())))
visited = [[ False for i in range(M+1)] for j in range(N+1)]
for i in range(N) :
    visited[i][0] = True
for i in range(M):
    visited[0][i] = True

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,-1,0,1]

visited[x][y] = True

count = 1
turn_time = 0
while(True):
    turn_left()
    nx = x+dx[direct]
    ny = y+dy[direct]
    if(visited[nx][ny]==False and gameMap[nx][ny]==0):
        visited[nx][ny] = True
        x = nx
        y = ny
        count+=1
        turn_time =0
        continue
    else:
        turn_time+=1
    if(turn_time==4):
        nx=x-dx[direct]
        ny = y-dy[direct]
        if(gameMap[nx][ny]==0):
            x =nx
            y = ny
        else:
            break
        turn_time=0
print(count)