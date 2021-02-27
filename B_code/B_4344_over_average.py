import sys
T = int(sys.stdin.readline())
for i in range(0,T):
    putin = sys.stdin.readline().split()
    N = int(putin[0])
    score_L = []
    sum_score = 0;
    for j in range(0,N):
        score_L.append(int(putin[j+1]))
        sum_score+=score_L[j]
    average_score = sum_score/N
    over_score_people =0
    for k in range(0,N):
        if(score_L[k]>average_score):
            over_score_people+=1
    print("%0.3f" %(over_score_people/N*100) ,end='')
    print("%", end = "\n")