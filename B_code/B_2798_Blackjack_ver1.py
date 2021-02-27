import sys
N,M = map(int, sys.stdin.readline().split())
index = list(map(int, sys.stdin.readline().split()))

case = []

for i in range (0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            case.append(index[i]+index[j]+index[k])

similar = -1;
for i in range(0, len(case)):
    if((case[i]<=M) & (abs(M-case[i]) < abs(M-similar))):
        similar = case[i]

print(similar)