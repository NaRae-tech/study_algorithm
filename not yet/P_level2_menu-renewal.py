import itertools
def solution(orders, course):
    answer =[]
    single = []
    for order in orders:
        for i in range(len(order)):
            if order[i] not in single:
                single.append(order[i])

    for c in course:
        menu = itertools.combinations(single,c)
        temp = []
        for m in menu:
            cnt = 0
            for order in orders:
                if set(order) & set(m) == set(m):
                    cnt+=1
            if cnt>=2:
                temp.append([m,cnt])
        if not(not temp):
            temp = sorted(temp, key=lambda x:x[1], reverse=True)
            maxi = temp[0][1]
            for t in temp:
                if t[1]>=maxi:
                    answer.append(''.join(sorted(t[0])))
                else:
                    break

    return sorted(answer)

orders=["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))