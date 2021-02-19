import sys
import math
A,B = sys.stdin.readline().split()

breakA = list(A)
breakB = list(B)

while(len(breakA)!=len(breakB)):
    if(len(breakA)>len(breakB)):
        breakB.insert(0,"0")
    else:
        breakA.insert(0,"0")

breakIA = []
breakIB = []
for i in range(len(breakA)-1,-1,-1):
    breakIA.insert(0,int(breakA[i]))
    breakIB.insert(0,int(breakB[i]))

answer= []
for i in range(len(breakA)-1,0,-1):
    if(breakIA[i]+breakIB[i]>=10):
        answer.insert(0,(breakIA[i]+breakIB[i])%10)
        breakIA[i-1] += math.floor((breakIA[i]+breakIB[i])/10)
    else:
        answer.insert(0,breakIA[i] + breakIB[i])
answer.insert(0,breakIA[0]+breakIB[0])

for i in range(len(answer)):
    print(answer[i],end='')