import sys
N = int(sys.stdin.readline())
direct = list(map(str,sys.stdin.readline().split()))
x,y =1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['U','D','L','R']
for item in direct:
    for i in range(0,4):
        if(item==move_type[i]):
            nx = x+dx[i]
            ny = y+dy[i]
    if(nx<1 or nx>N or ny<1 or ny>N):
        continue
    x,y=nx,ny
print(x,y)