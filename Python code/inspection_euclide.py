def gcd(a,b):
    while(b!=0):
        a,b= b,a%b
    return a

import sys
T = int(sys.stdin.readline())
numbers = []

for i in range(T):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

common = numbers[1]-numbers[0]
for i in range(1,T):
    common = gcd(common,numbers[i]-numbers[i-1])

commonList=[common]
for i in range(2,int((common**0.5)+1)):
    if(common%i==0):
        print(i,end=' ')
        if(i!=common//i):
            commonList.insert(0,common//i)
for num in commonList:
    print(num,end = ' ')