n=15
t=20
m=2
p=1

answer=''
if t==0:
    print(answer)
else:
    num = []
    for i in range(0,t*m):
        temp = []
        if n == 2:
            temp = list(bin(i)[2:])
        elif n==8:
            temp = list(oct(i)[2:])
        elif n==16:
            temp = list(hex(i)[2:])
        else:
            if i==0:
                temp=['0']
            else:
                while(i>0):
                    i,mod = i//n,i%n
                    if mod==10:
                        temp.append('A')
                    elif mod==11:
                        temp.append('B')
                    elif mod == 12:
                        temp.append('C')
                    elif mod == 13:
                        temp.append('D')
                    elif mod==14:
                        temp.append('E')
                    elif mod == 15:
                        temp.append('F')
                    else:
                        temp.append(str(mod))
                temp.reverse()
        num+=temp.copy()
    print(num)

    index = 0
    while(index<t):
        answer+=num[m*index+(p-1)]
        index+=1
    print(answer.upper())