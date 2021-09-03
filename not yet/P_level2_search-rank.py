from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []

    people = {}
    for i in range(len(info)):
        information = info[i].split(" ")
        for j in range(5):
            for c in combinations([0,1,2,3],j):
                temp = information[:-1].copy()
                for d in c:
                    temp[d] = "-"
                case = "/".join(temp)
                if case not in people:
                    people[case] = [int(information[4])]
                else:
                    people[case].append(int(information[4]))

    for q in query:
        cnt = 0
        que = q.replace(" and "," ").split(" ")
        condition = "/".join(que[:-1])
        if condition in people:
            value = sorted(people[condition])
            if value:
                cnt = len(value) - bisect_left(value, int(que[-1]))
                print(condition, value, cnt)
        answer.append(cnt)

    return answer

infomation = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
queries = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(infomation, queries))