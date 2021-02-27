N = int(input())

Nclass = 1
sum = 1
before = 1

while(sum<N):
    before = sum+1
    Nclass += 1
    sum += Nclass

if(Nclass==1):
    print(str(1) + "/" + str(1))
elif(Nclass%2==0):
    gap = sum-N
    print(str(Nclass-gap)+"/"+str(1+gap))
else:
    gap = N-before
    print(str(Nclass-gap)+"/"+str(1+gap))






