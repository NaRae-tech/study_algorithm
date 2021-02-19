import sys
import math
T = int(input())
for i in range(0,T):
    H,W,N = map(int, sys.stdin.readline().split())

    alreadyFull = math.floor(N/H)
    nowRoomN = alreadyFull+1
    nowRoomF = N-alreadyFull*H
    if (N%H==0):
        nowRoomN -= 1
        nowRoomF = H

    strF = str(nowRoomF)
    strN= str(nowRoomN)
    if(nowRoomN<10):
        strN="0"+strN

    print(strF+strN)