lottos = [45,4,35,20,3,9]
win_nums = [20,9,3,45,4,35]


right = 0
zero = lottos.count(0)
for item in lottos:
    if(item in win_nums):
        right+=1
ranking = [6,6,5,4,3,2,1]
answer = [ranking[right+zero], ranking[right]]
print(answer)