a = [1,2,3,4]
b=[-3,-1,0,2]

#방법1
print(sum(a*b for a,b in zip(a,b)))
#방법2
answer = 0
for i in range(0,len(a)):
    answer+=a[i]*b[i]
print(answer)