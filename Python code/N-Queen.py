count =0
arr = [[]]

def check(x,y,N):
 #arr에 있는 값들과 공격 가능성 있는지
    chess = [[False for i in range(N)] for j in range(N)]
    for a in range(0,len(arr)):
        X = arr[a][0]
        Y = arr[a][1]
        for i in range(N):
            chess[X][i] = True
            chess[i][Y] = True
        copyX = X
        copyY = Y
        while ((copyX > -1) & (copyY > -1)):
            chess[copyX][copyY] = True
            copyX -= 1
            copyY -= 1
        copyX = X
        copyY = Y
        while ((copyX < N) & (copyY < N)):
            chess[copyX][copyY] = True
            copyX += 1
            copyY += 1
        copyX = X
        copyY = Y
        while ((copyX > -1) & (copyY < N)):
            chess[copyX][copyY] = True
            copyX -= 1
            copyY += 1
        copyX = X
        copyY = Y
        while ((copyX < N) & (copyY > -1)):
            chess[copyX][copyY] = True
            copyX += 1
            copyY -= 1
    if(chess[x][y] == False):
        return True
    else:
        return False

def makeCount(N):
    global count
    global arr
    for i in range(0,N):
        for j in range(0,N):
            if (len(arr) == N):
                count+=1
                arr.clear()
            else:
                flag = check(i,j,N)
                if(flag==True):
                    arr.append([i,j])
                    makeCount(N)
                    arr.remove(len(arr)-1)
                else:
                    continue
import sys
N = int(sys.stdin.readline())
makeCount(N)
print(count)