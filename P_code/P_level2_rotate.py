def solution(sa):
    answer = 0
    for j in range(0, len(sa)):
        s =sa[j:len(sa)]+sa[0:j]
        flag = True
        stack = []
        for i in range(0,len(s)):
            if(s[i]=="[" or s[i]=="{" or s[i]=="("):
                stack.append(s[i])
            else:
                if((s[i] == "}" or s[i] == "]" or s[i] == ")") and not stack):
                    flag = False
                    break
                elif (s[i] == "}" and stack[-1] == "{"):
                    del stack[-1]
                elif (s[i] == "]" and stack[-1] == "["):
                    del stack[-1]
                elif (s[i] == ")" and stack[-1] == "("):
                    del stack[-1]
        if stack==[] and flag==True:
            answer += 1
    return answer

s = "}}}"
print(solution(s))