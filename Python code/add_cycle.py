count = 0
N=input()
if(int(N)<10):
    N="0"+N
copyN=N
newN=""
while(copyN!=newN):
    N1=N[0]
    N2=N[1]
    sumN = str(int(N1)+int(N2))
    if(int(sumN)<10):
        sumN="0"+sumN
    newN=N2+sumN[1]
    count+=1
    N = newN
print(count)