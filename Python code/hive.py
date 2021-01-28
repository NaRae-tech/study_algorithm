N = int(input())

step = 1
# N이 1일때
if(N==1):
    step =1

# N이 2이상 일때
else:
    start = 2
    next = 0
    while(True):
        next = start+6*step
        if(start<=N & N<next):
            step +=1
            break
        start = next
        step += 1


print(step)