new_id = "abcdefghijklmn.p"

import re
answer = new_id

answer = answer.lower()
print("1단계 : ", answer)

answer = re.sub('[^a-z0-9\-_.]','',answer)
print("2단계 : ", answer)

answer = re.sub('[.]+','.',answer)
print("3단계 : ", answer)

answer = re.sub('^[.]|[.]$','',answer)
print("4단계 : ", answer)

if(answer=="" or answer==None):
    answer+="a"
print("5단계 : ", answer)

if(len(answer)>=16):
    answer = answer[:15]
print("6단계 : ", answer)

if(len(answer)<=2):
    while(len(answer)<3):
        answer+=answer[-1]
print("7단계 : ", answer)