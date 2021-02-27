import sys
N = int(sys.stdin.readline())
reservation = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    reservation[i][0], reservation[i][1] = map(int,sys.stdin.readline().split())

reservation = sorted(reservation, key= lambda x:(x[1],x[0]))

count = 1
now = 0
for i in range(1,N):
    if(reservation[now][1]<=reservation[i][0]):
        count+=1
        now= i
print(count)