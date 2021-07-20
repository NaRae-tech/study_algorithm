citations = [88,89]

citations = sorted(citations)

answer = 0
for i in range(len(citations), -1, -1):
    count =0
    for j in range(0, len(citations)):
        if(citations[j]>=i):
            count+=1
    if(count>=i):
        if(answer<=i):
            answer=i
print(answer)