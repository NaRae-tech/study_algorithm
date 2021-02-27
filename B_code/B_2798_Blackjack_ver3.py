import sys
N,M = map(int, sys.stdin.readline().split())
index = list(map(int, sys.stdin.readline().split()))

case = 0;

for i in range (0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            this = index[i]+index[j]+index[k]
            if((this<=M)&(abs(M-case) > abs(M-this))):
                case = this

print (case)