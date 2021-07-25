nums = [1,2,7,4,6]
import itertools

#방법1
answer = 0
for item in itertools.combinations(nums,3):
    s = sum(item)
    flag = True
    for j in range(2,s):
        if(s%j ==0 ):
            flag = False
    if flag == True:
        answer+=1
print(answer)

#방법2
answer = -1
group = list(itertools.combinations(nums,3))
add = []
for item in group:
    add.append(sum(item))

prime_number = [True] * (max(add)+1)
m = int(max(add)**0.5)
for i in range(2, m+1):
    if(prime_number[i]==True):
        for j in range(i+i, max(add)+1, i):
            prime_number[j] = False

answer =0
for item in add:
    if(item!=0 and item!=1 and prime_number[item]==True):
        answer+=1
print(answer)