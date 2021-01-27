import sys
T=int(input())
real_test_score = list(map(int,sys.stdin.readline().split()))
max_score = real_test_score[0]
for i in range(0,T):
    if(max_score<real_test_score[i]):
        max_score = real_test_score[i]
modified_test_score = []
sum_score = 0
for j in range(0,T):
    modified_test_score.append(real_test_score[j]/max_score*100)
    sum_score = sum_score+modified_test_score[j]
print('%0.2f' %(sum_score/T))