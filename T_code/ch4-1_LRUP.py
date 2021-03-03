import sys
N = int(sys.stdin.readline())
direct = list(map(str, sys.stdin.readline().split()))
x=1
y=1
for item in direct:
    if(item=="L"):
        if (x-1>0):
            x-=1
    elif(item=="R"):
        if(x+1<N+1):
            x+=1
    elif(item =="U"):
        if(y-1>0):
            y-=1
    else:
        if(y+1<N+1):
            y+=1
print(str(y)+" "+str(x))
