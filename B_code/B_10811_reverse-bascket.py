n,m = list(map(int,input().split(' ')))
bascket = [i for i in range(1,n+1)]
while m>0:
    i,j = list(map(int,input().split(' ')))
    i,j = i-1,j-1
    temp = bascket[i:j+1]
    temp.reverse()
    bascket = bascket[:i]+temp+bascket[j+1:]
    m-=1
for k in bascket:
    print(k,end=' ')