answers = [1,3,2,4,2]

answer = []
p1 = [1,2,3,4,5]
p2 = [2,1,2,3,2,4,2,5]
p3 = [3,3,1,1,2,2,4,4,5,5]

c1 = 0
c2 = 0
c3 = 0
for i in range(0, len(answers)):
    if(p1[i%5] == answers[i]):
        c1+=1
    if(p2[i%8] == answers[i]):
        c2+=1
    if (p3[i%10] == answers[i]):
        c3 += 1

maximum = max(c1,c2,c3)
if(c1==maximum):
    answer.append(1)
if(c2==maximum):
    answer.append(2)
if(c3==maximum):
    answer.append(3)

answer = sorted(answer)
print(answer)