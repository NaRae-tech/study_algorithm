numbers = "17"

import itertools
num = list(map(int, numbers))

#2~n자리 조합 만들기
permuSet = []
for i in range(2, len(num)+1):
    permu = itertools.permutations(num, i)
    permu = list(set(permu))
    permuSet += permu

#1자리 조합 합하기 + 앞서 만든 조합 숫자로 만들기
numPermu = num
for i in range(0, len(permuSet)):
    numStr =""
    for j in range(0, len(permuSet[i])):
        numStr+=str(permuSet[i][j])
    numPermu.append(int(numStr))
numPermu = list(set(numPermu))

#에라토스테네스의 체-> 소수는 true, 아니면 false
boolPermu = [True] * (max(numPermu)+1)
m = int(max(numPermu)**0.5)
for i in range(2,m+1):
    if(boolPermu[i] == True):
        for j in range(i*i,max(numPermu)+1,i):
            boolPermu[j] = False

#소수인지 확인
answer = 0
for n in numPermu:
    if(n==0 or n==1):
        pass
    else:
        if(boolPermu[n]==True):
            answer+=1
print(answer)