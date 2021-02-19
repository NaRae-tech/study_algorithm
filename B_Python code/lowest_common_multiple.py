def gcd(a,b):
    while(b!=0):
        a,b=b,a%b
    return a

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(int(A*B/gcd(A,B)))