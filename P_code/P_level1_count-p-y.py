s = "aBvd"

#방법 1
s = s.lower()
answer = True
if(s.count('p')!=s.count('y')):
    answer = False
print(answer)

#방법 2
print(s.lower().count('p')==s.lower().count('y'))