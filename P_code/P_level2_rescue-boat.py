def solution(people, limit):
    answer =0
    people.sort()
    maxi = -1
    mini = 0
    while(mini-len(people) <= maxi):
        answer += 1
        if (people[maxi] + people[mini] <= limit):
            mini += 1
        maxi -= 1
    return answer

from collections import deque
def solutions(people, limit):
    deqp = deque(sorted(people))
    answer = 0
    while(len(deqp)>0):
        answer+=1
        if(len(deqp)>1):
            if(deqp[0]+deqp[-1]<=limit):
                deqp.popleft()
            deqp.pop()
        else:
            deqp.pop()
    return answer

people = [70,50,80,50]
limit = 100
print(solutions(people, limit))