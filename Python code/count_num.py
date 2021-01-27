num1=int(input())
num2=int(input())
num3=int(input())
num = num1*num2*num3
char = list(str(num))
numL = list(map(int, char))
count = [0 for i in range(10)]
for i in range(0,len(numL)):
    count[numL[i]]=count[numL[i]]+1
for j in range(0,10):
    print(count[j])