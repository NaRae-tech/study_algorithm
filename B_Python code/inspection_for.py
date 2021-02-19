import sys
T = int(sys.stdin.readline())
numbers = [0 for _ in range(T)]
max = 0
for i in range(0,T):
    N = int(sys.stdin.readline())
    numbers[i] = N
    if(N>max) : max = N

for i in range(2,max+1):
    flag = False
    rest = numbers[0]%i
    for j in range(1,T):
        if((numbers[j]%i)==rest):
            flag = True
        else:
            flag = False
            break
    if(flag==True):
        print(i, end=' ')