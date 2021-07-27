participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion= ["josipa", "filipa", "marina", "nikola"]

#방법 1
temp = 0
dict = {}
for par in participant:
    dict[hash(par)] = par
    temp += int(hash(par))
for com in completion:
    temp-= hash(com)
print(dict[temp])

#방법 2
import collections
answer = collections.Counter(participant)-collections.Counter(completion)
print(list(answer.keys())[0])

#방법 3
participant.sort()
completion.sort()
answer = ''
for i in range(len(completion)):
    if(participant[i]!=completion[i]):
        answer = participant[i]
if(answer==''):
    answer = participant[-1]
print(answer)