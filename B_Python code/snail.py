import sys
import math
A,B,V = map(int, sys.stdin.readline().split())

day = math.floor((V-A)/(A-B))
height = (A-B)*day

while(True):
    if(V<=height):
        print(day)
        break
    elif(height>1000000000):
        print(day-1)
        break
    day+=1
    height+=A
    if (V <= height):
        print(day)
        break
    elif (height > 1000000000):
        print(day - 1)
        break
    height-=B