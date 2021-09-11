def solution(n, k):
    answer = 0

    num = ""
    if k == 10:
        num = str(n)
    else:
        changeN=[]
        while n>0:
            changeN.append(str(n%k))
            n//=k
        changeN.reverse()
        num = ''.join(changeN)

    while "00" in num:
        num = num.replace("00","0")

    prime= list(map(int,num.split('0')))

    net = [ True for i in range(max(prime)+1)]
    for i in range(2, max(prime)//2+1):
        if net[i] == True:
            for j in range(i+i, max(prime)+1, i):
                net[j] = False

    for p in prime:
        if p>1 and net[p]:
            answer+=1
    return answer

n = 1100011
k = 10
print(solution(n,k))