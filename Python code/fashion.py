import sys
from collections import Counter
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    item = []
    for i in range(N):
        name, kind = sys.stdin.readline().split()
        item.append(kind)
    sortItem = Counter(item)
    result =1
    for i in range(N):
        result*=(sortItem[i]+1)
    print(result-1)