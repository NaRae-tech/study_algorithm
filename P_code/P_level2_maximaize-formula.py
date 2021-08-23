import re
from itertools import permutations
def solution(expression):
    signs = [x for x in ['*','-','+'] if x in expression]
    signs = [list(p) for p in permutations(signs)]
    formula = re.split(r'(\D)',expression)

    answer = []
    for sign in signs:
        formu = formula[:]
        for s in sign:
            while s in formu:
                temp = formu.index(s)
                formu[temp-1] = str(eval(formu[temp-1]+formu[temp]+formu[temp+1]))
                formu = formu[:temp]+formu[temp+2:]
        answer.append(formu[-1])

    return max(abs(int(x))for x in answer)


import re
from itertools import permutations
from collections import deque
def calculate(num1,num2,sign):
    if sign=='+':
        return num1+num2
    elif sign=='-':
        return num1-num2
    else:
        return num1*num2

def solution2(expression):
    answer = []
    num = list(map(int,re.findall('\d+',expression)))
    sign = re.findall('\d+([\+]?[\-]?[\*]?)',expression)

    signper = list(permutations(set(sign[:-1]),len(set(sign[:-1]))))
    for case in signper:
        formula = []
        for i in range(len(num)):
            formula.append(num[i])
            formula.append(sign[i])
        stack = deque(formula[:-1])
        result = deque()
        print('cccccc',formula,stack,result)
        print(case)
        for c in case:
            print(c, stack, result)
            for i in range(0, len(stack)):
                if i==0:
                    result.append(stack[0])
                elif stack[i-1]!=c:
                    result.append(stack[i])
                else:
                    s = result.pop()
                    n1 = result.pop()
                    result.append(calculate(n1,stack[i],s))
            stack.clear()
            stack = result.copy()
            result.clear()
        print(stack)
        answer.append(stack.popleft())
        print(answer)
    for i in range(len(answer)):
        answer[i] = abs(answer[i])
    return max(answer)

expression = "50*6-3*2"
print(solution(expression))