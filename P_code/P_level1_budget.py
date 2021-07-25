d=[1,3,2,5,4]
budget = 9

#방법1
d.sort()
while(budget<sum(d)):
    d.pop()
print(len(d))


#방법2
d.sort()
answer = 0
for item in d:
    budget-=item
    if(budget>=0):
        answer+=1
print(answer)

#방법3
d.sort()
answer = 0
sum = 0
for item in d:
    sum += item
    if(sum<=budget):
        answer+=1
print(answer)