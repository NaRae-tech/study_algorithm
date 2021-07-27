dartResult = "1D2S3T*"

#방법 1
import re
bonus = {'S':1, 'D':2, 'T':3}
option = {'':1, '*':2,'#':-1}
d = re.compile('(\d+)([SDT])([*#]?)')
dart = d.findall(dartResult)
for i in range(0,len(dart)):
    if(dart[i][2]=='*' and i>0):
        dart[i-1]*=2
    dart[i] = int(dart[i][0])**bonus[dart[i][1]]*option[dart[i][2]]
print(sum(dart))


#방법 2
answer = 0
score = []
for i in range(len(dartResult)):
    if (dartResult[i] == 'S'):
        score[-1] = score[-1] ** 1
    elif(dartResult[i] == 'D'):
        score[-1] = score[-1]**2
    elif (dartResult[i] == 'T'):
        score[-1] = score[-1] ** 3
    elif (dartResult[i] == '*'):
        if len(score)==1:
            score[-1] *=2
        else:
            score[-1]*=2
            score[-2]*=2
    elif (dartResult[i] == "#"):
        score[-1] *= -1
    else:
        if(i>0 and dartResult[i-1]=='1' and dartResult[i]=='0'):
            score[-1]=int(dartResult[i-1]+dartResult[i])
        else:
            score.append(int(dartResult[i]))
print(sum(score))