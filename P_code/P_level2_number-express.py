n = 15

temp = [i for i in range(0,n+1)]
count =0
for i in range(1,n+1):
    answer = temp[i]
    if (answer == n):
        count += 1
    else:
        for j in range(i+1,n+1):
            answer += temp[j]
            if(answer==n):
                count+=1
            elif answer>n:
                break
print(count)