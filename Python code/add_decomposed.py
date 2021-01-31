target = int(input())

check = 0;
for i in range(0,target+1):
    sum = i
    for j in range(0,len(str(i))):
        sum += int(str(i)[j])
    if sum == target:
        check = i
        break

print(check)