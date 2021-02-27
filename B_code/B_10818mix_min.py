import sys
T=int(sys.stdin.readline())
N= list(map(int,sys.stdin.readline().split()))
max = N[0]
min = N[0]
for i in range(1,T):
    if(max<N[i]):
        max = N[i]
    if(min>N[i]):
        min = N[i]
print(str(min)+" "+str(max))
