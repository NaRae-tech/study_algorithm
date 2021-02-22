import sys
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    commend = sys.stdin.readline().split()
    if(commend[0] == "push"):
        num = int(commend[1])
        numbers.insert(0,num)
    elif(commend[0]=="pop"):
        if(len(numbers)==0):
            print(-1)
        else:
            print(numbers[0])
            del numbers[0]
    elif (commend[0] == "size"):
        print(len(numbers))
    elif (commend[0] == "empty"):
        if(len(numbers) ==0):
            print(1)
        else :
            print(0)
    elif(commend[0]=="top"):
        if (len(numbers) == 0):
            print(-1)
        else:
            print(numbers[0])
