check = []
def push(a:str):
    check.insert(0,a)
def pop():
    del check[0]
def size():
    return len(check)

import sys
N = int(sys.stdin.readline())

for _ in range(N):
    check.clear()

    exam = sys.stdin.readline()
    flag = True
    for i in range(len(exam)-1):
        if(exam[i] == '('):
            push(exam[i])
        else :
            if(size()==0):
                flag = False
                break
            else:
                pop()

    if((flag == True) and (size()==0)):
        print("YES")
    else:
        print("NO")