n = 5

temp = set(range(2,n+1))
for i in range(2,n//2+1):
    if i in temp:
        temp-=set(range(i+i,n+1,i))
print(len(temp))

net = [True]*(n+1)
for i in range(2,n//2+1):
    if(net[i]==True):
        for j in range(i+i,n+1,i):
            net[j]=False
print(net[2:n+1].count(True))