def check(chess, columnR, rowR):
    #짝수 칸이 W일 때
    changeCountW = 0
    #짝수 칸이 B일 때
    changeCountB = 0
    for i in range(rowR,8+rowR):
        for j in range(columnR,8+columnR):
            if(((i+j)%2 == 1) & (chess[i][j]!="B")):
                changeCountW+=1
            elif(((i+j)%2 == 0) & (chess[i][j]!="W")):
                changeCountW+=1
            if (((i + j) % 2 == 1) & (chess[i][j] != "W")):
                changeCountB += 1
            elif (((i + j) % 2 == 0) & (chess[i][j] != "B")):
                changeCountB += 1
    if (changeCountW>changeCountB):
        return changeCountB
    return changeCountW

import sys
M,N = map(int, sys.stdin.readline().split())

chess = list()
for i in range(0,M):
    chess.append(sys.stdin.readline())

list = list()
for i in range(0,M-7):
    for j in range(0,N-7):
        list.append(check(chess,j,i))

minimum = 64
for item in list:
    if(item<minimum):
        minimum = item

print(minimum)