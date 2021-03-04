import sys
now = sys.stdin.readline()
x = int(ord(now[0])-ord('a'))+1
y = int(now[1])
count =0
step = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
for i in range(len(step)):
    tempX = x+step[i][0]
    tempY = y+step[i][1]
    if(0<tempX and tempX<9 and 0<tempY and tempY<9):
        count+=1
print(count)