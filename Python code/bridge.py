import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().split())
    fascal = [[1 for _ in range(M+1)]for _ in range(M+1)]
    for i in range(0,M+1):
        for j in range(0,i+1):
            if((i==j) | (j==0)):
                fascal[i][j] = 1
            else:
                fascal[i][j] = fascal[i-1][j-1]+fascal[i-1][j]
    print(fascal[M][N])