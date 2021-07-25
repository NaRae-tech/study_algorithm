s = "1234"

answer = True
if(len(s)!=4 and len(s)!= 6):
    answer = False
for item in s:
    if(ord(item)>57 or 48>ord(item)):
        print(item, ord(item))
        answer = False
print(answer)