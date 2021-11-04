a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
second = 0
status = True
while a!=b:
    if a<0 and status:
        second+=c
        a+=1
    elif a==0 and status:
        second+=d
        status = False
    else:
        second+=e
        a+=1
print(second)