import math
def findTime(mineral, weight, time,i):
    return math.ceil(mineral[i] / weight[i]) * 2 * time[i] - time[i]

def transper(target, mineral, weight ,time):
    K = [[0 for i in range(target+1)]for j in range(len(mineral)+1)]
    for i in range(len(mineral)+1):
        for j in range(target+1):
            if i == 0 or j ==0:
                K[i][j] = 0
            elif mineral[i-1]<=target:
                K[i][j] = max(findTime(mineral,weight,time,i-1)+K[i-1][target-mineral[i-1]], K[i-1][target])
            else:
                K[i][j] = K[i-1][j]
    print(K)
    return K[len(mineral)][target]

def solution(a, b, g, s, w, t):
    gold = transper(a,g,w,t)
    silver = transper(b,s,w,t)
    return max(gold, silver)

"""
def solution(a,b,g,s,w,t):
    answer = 0
    weightPerTime = {i : w[i]/t[i] for i in range(len(w))}
    weightPerTime = sorted(weightPerTime.items(), key=lambda x:x[1], reverse=True)

    getG = [0 for i in range(len(g))]
    getS = [0 for i in range(len(s))]
    

    for i in range(len(getG)):
        if getG[i]!=0:
            getG[i] = getG[i]*2*t[i]-t[i]
        if getS[i]!=0:
            getS[i] = getS[i]*2*t[i]-t[i]
    return max([max(getS),max(getS)])

"""
a = 10
b = 10
g = [100]
s=[100]
w =[7]
t = 10
print(solution(a,b,g,s,w,t))