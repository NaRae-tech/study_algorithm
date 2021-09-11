import sys
T = int(sys.stdin.readline())
R= [[0 for _ in range(2)] for _ in range(T)]
G= [[0 for _ in range(2)] for _ in range(T)]
B= [[0 for _ in range(2)] for _ in range(T)]
for i in range(T):
    R[i][0],G[i][0],B[i][0] = map(int, sys.stdin.readline().split())
    R[i][1] = i
    G[i][1] = i
    B[i][1] = i
R = sorted(R, key = lambda x:(x[0],x[1]));
G = sorted(G, key = lambda x:(x[0],x[1]));
B = sorted(B, key = lambda x:(x[0],x[1]));

colored = ['n' for _ in range(T)]
price = 0
count = 0
while(count<T):
    print(colored)
    print(R)
    print(G)
    print(B)
    if(len(R)!=0):
        minimum = R[0][0]
        minimumInd = R[0][1]
        minimumcolor = 'R'
    else:
        if(len(G)!=0):
            minimum = G[0][0]
            minimumInd = G[0][1]
            minimumcolor = 'G'
        else:
            minimum = B[0][0]
            minimumInd = B[0][1]
            minimumcolor = 'B'
    if(len(R)!=0 and R[0][0]<minimum):
        minimum = R[0][0]
        minimumInd = R[0][1]
        minimumcolor = 'R'
    elif (len(G)!=0 and G[0][0]<minimum):
        minimum = G[0][0]
        minimumInd = G[0][1]
        minimumcolor = 'G'
    elif(len(B)!=0 and B[0][0]<minimum):
        minimum = B[0][0]
        minimumInd = B[0][1]
        minimumcolor = 'B'

    if(colored[minimumInd] == 'n'):
        if(minimumInd==0):
            if(colored[minimumInd+1]!=minimumcolor):
                colored[minimumInd] = minimumcolor
                price+=minimum
                count+=1
        elif(minimumInd==T-1):
            if (colored[minimumInd - 1] != minimumcolor):
                colored[minimumInd] = minimumcolor
                price += minimum
                count += 1
        else:
            if (colored[minimumInd + 1] != minimumcolor and colored[minimumInd - 1] != minimumcolor):
                colored[minimumInd] = minimumcolor
                price += minimum
                count += 1
    if (minimumcolor == 'R'): del R[0]
    elif (minimumcolor == 'G'): del G[0]
    elif (minimumcolor == 'B'): del B[0]
print(price)