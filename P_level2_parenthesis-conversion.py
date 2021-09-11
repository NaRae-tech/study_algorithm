def divide(p):
    temp = 0
    for i in range(len(p)):
        if p[i]=='(':
            temp+=1
        else:
            temp-=1
        if temp==0:
            return p[:i+1], p[i+1:]
def checking(s):
    stack = []
    for i in range(len(s)):
        if s[i]==')' and not stack:
            return False
        elif s[i] == '(':
            stack.append('(')
        else:
            stack.pop()
    if not stack:
        return True
    return False

def solution(p):
    answer = ''

    return answer


p = "()))((()"
print(solution(p))