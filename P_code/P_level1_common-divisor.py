n=3
m=12

#방법 1
a,b = max(n,m), min(n,m)
c = 1
answer=[]
while(c>0):
    c=a%b
    a,b = b,c
answer = [a,int(n*m/a)]
print(answer)

#방법2
import math
print([math.gcd(n,m),n*m//math.gcd(n,m)])