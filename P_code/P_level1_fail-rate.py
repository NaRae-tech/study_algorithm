n = 5
stages = [2,1,2,6,2,4,3,3]

#방법1
answer = {}
people = len(stages)
for stage in range(1, n+1):
    if(people==0):
        answer[stage]=0
    else:
        participate = stages.count(stage)
        answer[stage] = participate / people
        people -= participate
print(sorted(answer, key=lambda x : answer[x], reverse=True))

#방법2
people = len(stages)
level = []
for i in range(1,n+1):
    level.append(stages.count(i));
print(level)

rates = []
for i in range(0,n):
    if people==0:
        rates.append(0)
    else:
        rates.append(level[i]/people)
        people-=level[i]
print(rates)

sortedRates = sorted(rates,reverse=True)
print(sortedRates)

answer=[]
for i in range(0,n):
    for j in range(0,n):
        if(sortedRates[i]==rates[j]):
            answer.append(j+1)
            rates[j]=-1
            break
print(answer)