import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N,M= map(int,sys.stdin.readline().split())
    total =1
    if(N!=M):
        for i in range(M,M-N,-1):
            total*=i
        for j in range(N,1,-1):
            total//=j
    print(total)