rest=[0 for i in range(0,42)]
for j in range(0,10):
    num = int(input())
    rest[num%42]+=1
count = 0
for k in range(0,len(rest)):
    if(rest[k]!=0):
        count+=1
print(count)