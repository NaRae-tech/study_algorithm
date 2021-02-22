numbers = []
def size():
    print(len(numbers))
def push(a):
    numbers.insert(0,a)
def pop():
    if(len(numbers)==0):
        print(-1)
    else:
        print(numbers[0])
        del numbers[0]
def empty():
    if(len(numbers)==0):
        print(1)
    else:
        print(0)
def top():
    if (len(numbers) == 0):
        print(-1)
    else:
        print(numbers[0])
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    commend = sys.stdin.readline().split()
    if(commend[0] == "push"):
        push(commend[1])
    elif(commend[0] == "pop"):
        pop()
    elif (commend[0] == "size"):
        size()
    elif (commend[0] == "empty"):
        empty()
    elif (commend[0] == "top"):
        top()