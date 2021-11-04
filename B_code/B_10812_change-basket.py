n,m = list(map(int, input().split(' ')))
bascket = [i for i in range(1,n+1)]
for i in range(0,m):
    begin, end, mid = list(map(int,input().split(' ')))
    begin, end, mid = begin-1, end-1, mid-1
    temp = bascket[mid:end+1]+bascket[begin:mid]
    bascket = bascket[:begin]+temp+bascket[end+1:]
for b in bascket:
    print(b,end=' ')