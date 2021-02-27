check = []
def push(a):
    check.insert(0,a)
def pop():
    del check[0]
def size():
    return len(check)
def top():
    return check[0]
import sys
while(True):
    check.clear()
    exam = sys.stdin.readline()
    if(exam ==".\n"):
        break
    flag = True
    for i in range(len(exam)-1):
        if(exam[i] == '('):
            push('(')
        elif(exam[i] == '['):
            push('[')
        elif(exam[i] == ')'):
            if(size()==0):
                flag = False
                break
            else:
                if(top()=='('):
                    pop()
                else:
                    flag = False
                    break
        elif (exam[i] == ']'):
            if (size() == 0):
                flag = False
                break
            else:
                if (top() == '['):
                    pop()
                else:
                    flag = False
                    break
    if((flag == True) and (size()==0)):
        print("yes")
    else:
        print("no")