visited = [False for _ in range(21)]
arr = [ -1 for _ in range(21)]
memberList = []
def memberCheck(now:int, N):
    global visited
    global arr
    global memberList
    if(now==(N/2+1)):
        team1 = []
        for i in range(1,now):
            team1.append(arr[i])
        memberList.append(team1)
    else:
        for i in range(0,N):
            if(visited[i]==True):
                continue
            else:
                if(i>arr[now-1]):
                    arr[now] = i
                    visited[i] = True
                    memberCheck(now+1,N)
                    visited[i] = False

import sys
# 총 인원수
N = int(sys.stdin.readline())
# 사람 별 능력치 입력받기
peopleCapa = []
for _ in range(N):
    peopleCapa.append(list(map(int, sys.stdin.readline().split())))
# 팀 나눌 수 있는 경우 나열
memberCheck(1,N)
# 두팀으로 나누기
caseCount = int(len(memberList) / 2)
startT = []
linkT =[]
for i in range(0,caseCount):
    startT.append(memberList[i])
    linkT.append(memberList[(len(memberList)-1)-i])
#팀별 capa합 구하기
memberCapaCalcul = [[0 for _ in range(2)]for _ in range(caseCount)]
for k in range(0,caseCount):
    for i in range(0,int(N/2)):
        for j in range(0,int(N/2)):
            memberCapaCalcul[k][0]+=peopleCapa[(startT[k])[i]][(startT[k])[j]]
            memberCapaCalcul[k][1] += peopleCapa[(linkT[k])[i]][(linkT[k])[j]]
#팀별 capa차이가 가장 작은 경우 구하기
minimum = 1000
for i in range(0,caseCount):
    capaG = abs(memberCapaCalcul[i][1]-memberCapaCalcul[i][0])
    if(minimum>capaG):
        minimum = capaG
print(minimum)