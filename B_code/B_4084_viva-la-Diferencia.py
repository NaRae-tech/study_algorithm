a,b,c,d = list(map(int,input().split(' ')))
while not(a==0 and b==0 and c==0 and d==0):
    count = 0
    while True:
        if a==b and b==c and c==d:
            break
        a,b,c,d = abs(a-b),abs(b-c),abs(c-d),abs(d-a)
        count+=1
    print(count)
    a, b, c, d = list(map(int, input().split(' ')))