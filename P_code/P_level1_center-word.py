s = "abcde"

#방법1
print(s[(len(s)-1)//2:len(s)//2+1])

#방법2
answer=''
if(len(s)%2==0):
    answer = s[len(s)//2-1]+s[len(s)//2]
else:
    answer = s[len(s)//2]
print(answer)