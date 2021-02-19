global apart
T = int(input())
while(T!=0):
    Floor = int(input())
    Number = int(input())
    apart = [[0 for i in range(Number+1)]for j in range(Floor+1)]
    for a in range(0,Floor+1):
        if(a==0):
            for b in range(0,Number+1):
                apart[a][b] = b

    for a in range(1,Floor+1):
        for b in range(1, Number+1):
            apart[a][b] = apart[a-1][b]+apart[a][b-1]
    print(apart[Floor][Number])

    T-=1
    apart.clear()