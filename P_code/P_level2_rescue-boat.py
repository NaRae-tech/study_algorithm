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


people = [70,50,80,50]
limit = 100
print(solution(people, limit))