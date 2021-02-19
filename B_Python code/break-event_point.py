import sys
import math
A, B, C = map(int, sys.stdin.readline().split())
if (B>=C):
    print(-1)
else :
    if(A%(-B+C) == 0):
        print (math.ceil(A/(-B+C)+1))
    else:
        print(math.ceil(A/(-B+C)))