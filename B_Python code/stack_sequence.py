stack = [0]
def push(a):
    print("+")
    stack.insert(0,a)
def pop():
    print("-")
    del stack[0]
def top():
    return stack[0]

import sys
N = int(sys.stdin.readline())

want = []
for _ in range(N):
    want.append(int(sys.stdin.readline()))

flag =True
check = [False for _ in range(len(want)+1)]
for i in range(0, len(want)-1):
    if(flag == True):
        check[want[i]] = True
        check[want[i+1]] = True
        if(want[i]>want[i+1]):
            for j in range(want[i+1],want[i]):
                if(check[j]==False):
                    flag = False


if(flag == False):
    print("NO")
else:
    now = 0
    while(len(want)!=0):
        now+=1
        push(now)
        while(True):
            if((len(want)!=0)and (top()==want[0])):
                pop()
                del want[0]
            else:
                break