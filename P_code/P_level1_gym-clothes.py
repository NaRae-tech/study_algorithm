n = 5
lost = [1,2,3,4]
reserve = [3,4,5]

lost.sort()
reserve.sort()
answer = n-len(lost)
ln = len(lost)-1
while(ln>=0):
    if(lost[ln] in reserve):
        answer+=1
        del reserve[reserve.index(lost[ln])]
        del lost[ln]
    ln-=1

for i in range(0, len(lost)):
    if lost[i]-1 in reserve:
        answer += 1
        del reserve[reserve.index(lost[i]-1)]
    elif lost[i]+1 in reserve:
        answer += 1
        del reserve[reserve.index(lost[i]+1)]

print(answer)