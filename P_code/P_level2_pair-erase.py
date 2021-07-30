s = "baabaa"

stack = []
for i in range(0,len(s)):
    if not stack:
        stack.append(s[i])
    else:
        if stack[-1]!=s[i]:
            stack.append(s[i])
        else:
            stack.pop()
print(int(not(stack)))
