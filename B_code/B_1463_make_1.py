import sys
N = int(sys.stdin.readline())
d = [0 for _ in range(N+1)]
for i in range(2,N+1):
    d[i]=d[i-1]+1
    if(i%3==0 and d[i//3]+1<d[i]):
        d[i] = d[i//3]+1
    elif(i%2==0 and d[i//2]+1<d[i]):
        d[i] = d[i//2]+1
print(d)
print(d[N])

