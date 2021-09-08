def change(n):
    sn = str(n)
    if len(sn) == 4:
        return sn[:-1]
    elif len(sn) == 3:
        return sn
    elif len(sn)==2:
        if sn[0]<sn[1]:
            return sn+str(int(sn[0])+1)
        else:
            return sn+sn[0]
    else:
        return sn*3

def solution(numbers):
    numbers.sort(key=lambda x:(change(x),len(str(x))),reverse=True)
    numbers = list(map(str, numbers))
    for i in range(100):
        for j in range(11):
            print(numbers[i*10+j],end = ' ')
        print('')
    return ''.join(numbers)

numbers = [i for i in range(0,1001)]
print(solution(numbers))