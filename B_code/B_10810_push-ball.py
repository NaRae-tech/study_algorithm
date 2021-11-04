n,m = list(map(int,input().split(' ')))
bascket = [0 for i in range(0,n)]
while m>0:
    i,j,k = list(map(int,input().split(' ')))
    for a in range(i-1,j):
        bascket[a] = k
    m-=1
for ball in bascket:
    print(ball,end=' ')