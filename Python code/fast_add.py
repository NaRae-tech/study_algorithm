import sys

T=int(input())
for line in sys.stdin:
    x, y = line.split()
    x = int(x)
    y = int(y)
    print(x+y)
