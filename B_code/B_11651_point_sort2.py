import sys

T = int(sys.stdin.readline())
list = [[0 for i in range(0,2)] for j in range(0,T)]
for i in range(0,T):
    list[i][0], list[i][1] = map(int, sys.stdin.readline().split())
list.sort(key = lambda list: (list[1],list[0]))

for i in range(0,T):
    print(list[i][0],end=" ")
    print(list[i][1],end= "\n")