def solution(info, query):
    answer = []
    people = [list(information.split(' ')) for information in info]
    people.sort(key=lambda x:int(x[4]))

    for q in query:
        c = q.replace(' and', '').split(' ')
        left = 0
        right = len(people)-1

        while left<right:
            middle = (left + right) // 2
            if int(people[middle][4])==int(c[4]):
                break
            elif int(people[middle][4])>int(c[4]):
                right=middle
            elif int(people[middle][4])<int(c[4]):
                left =middle+1

        cnt = 0
        for i in range(middle, len(people)):
            if ((c[0] == '-' or c[0] == people[i][0])
                    and (c[1] == '-' or c[1] == people[i][1])
                    and (c[2] == '-' or c[2] == people[i][2])
                    and (c[3] == '-' or c[3] == people[i][3])
                    and int(c[4])<=int(people[i][4])):
                cnt+=1
        answer.append(cnt)

    return answer

infomation = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
queries = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(infomation, queries))