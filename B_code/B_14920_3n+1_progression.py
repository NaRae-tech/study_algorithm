c = int(input())
progression = []
count = 1
progression.append(c)
while c !=1:
    if c%2==0:
        c=c/2
    else:
        c=3*c+1
    progression.append(c)
    count+=1
print(count)
