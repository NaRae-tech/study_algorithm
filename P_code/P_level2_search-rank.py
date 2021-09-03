def solution0(info, query):
    answer =[]
    people = [information.split(" ") for information in info]
    for q in query:
        que = q.replace(' and ',' ').split(" ")
        cnt = 0
        for i in range(len(people)):
            if((que[0] =='-' or que[0]==people[i][0])
            and (que[1] =='-' or que[1]==people[i][1])
            and (que[2] == '-' or que[2] == people[i][2])
            and (que[3] == '-' or que[3] == people[i][3])
            and (int(que[4])<=int(people[i][4]))):
                cnt+=1
        answer.append(cnt)
    return answer

#방법 1
from itertools import combinations
def solution1(info, query):
    answer = []
    people = {}
    for information in info:
        splitInfo = information.split(" ")
        for j in range(5):
            com = list(combinations([0,1,2,3],j))
            for c in com:
                temp = splitInfo[:-1].copy()
                for d in c:
                    temp[d] = "-"
                case = "/".join(temp)
                if case in people:
                    people[case].append(int(splitInfo[-1]))
                else:
                    people[case] = [int(splitInfo[-1])]
    for key in people.keys():
        people[key].sort()

    for q in query:
        cnt = 0
        que = q.replace(' and ',' ').split(" ")
        condition = "/".join(que[:-1])
        target = int(que[-1])
        if condition in people:
            value = people[condition]
            if value:
                left, right = 0, len(value)
                while left < right:
                    middle = (left+right)//2
                    if value[middle]>=target:
                        right = middle
                    else:
                        left = middle+1
                cnt = len(value)-left
        answer.append(cnt)
    return answer

#방법 2
from itertools import combinations
from bisect import bisect_left
def solution2(info, query):
    answer = []

    people = {}
    for i in range(len(info)):
        information = info[i].split(" ")
        for j in range(5):
            for c in combinations(information[:-1],j):
                case = ''.join(c)
                if case not in people:
                    people[case] = [int(information[4])]
                else:
                    people[case].append(int(information[4]))

    for key in people.keys():
        people[key].sort()

    for q in query:
        cnt = 0
        que = q.replace(" and "," ").replace('-', '').split(" ")
        condition = "".join(que[:-1])
        if condition in people:
            value = people[condition]
            if value:
                cnt = len(value) - bisect_left(value, int(que[-1]))
        answer.append(cnt)

    return answer

infomation = ["java backend junior pizza 150"]
queries = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(infomation, queries))