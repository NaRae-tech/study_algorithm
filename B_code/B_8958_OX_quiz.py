import sys
T = int(sys.stdin.readline())
for j in range(0,T):
    answer = sys.stdin.readline()
    num_ans = len(answer)
    con = 0;
    score = 0;
    for i in range(0,num_ans):
        if(answer[i]=='O'):
            con += 1
            score+=con
        else:
            con = 0
    print(score)