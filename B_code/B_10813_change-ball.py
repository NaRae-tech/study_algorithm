n,m = list(map(int,input().split(' ')))
bascket = [i for i in range(1,n+1)]
while m>0:
    i,j = list(map(int,input().split(' ')))
    bascket[i-1], bascket[j-1] = bascket[j-1], bascket[i-1]
    m-=1
for k in bascket:
    print(k,end=' ')