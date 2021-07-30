s = "(())()"

#방법 1
def solution(s):
    answer = 0
    for i in range(0,len(s)):
        if s[i]=='(':
            answer+=1
        elif s[i]==')':
            answer -=1
        if answer<0:
            return False
    return answer==0
print(solution("(())()"))

#방법 2
stack = []
for i in range(0,len(s)):
    if(s[i]=='('):
        stack.append(s[i])
    elif (s[i]!='(' and not stack):
        stack.append(s[i])
        break
    else:
        if(stack[-1]=='('):
            del stack[-1]
print(not stack)