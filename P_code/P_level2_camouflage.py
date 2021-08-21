from collections import Counter
from functools import reduce
def solution1(clothes):
    count = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x,y:x*(y+1), count.values(),1)-1
    return answer

def solution(clothes):
    kind = {}
    for n, k in clothes:
        if k not in kind:
            kind[k] = 1
        else:
            kind[k] += 1

    answer = 1
    for value in list(kind.values()):
        answer*=(value+1)
    answer-=1
    return answer

#시간초과
from itertools import combinations
def solution2(clothes):
    answer =0

    kind = {}
    for n, k in clothes:
        if k not in kind:
            kind[k] = 1
        else:
            kind[k] += 1


    for i in range(1, len(kind)+1):
        com = list(combinations(list(kind.keys()), i))
        for i in range(len(com)):
            temp = 1
            for k in range(len(com[i])):
                temp*=kind[com[i][k]]
            answer+=temp

    return answer
clothes =[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))