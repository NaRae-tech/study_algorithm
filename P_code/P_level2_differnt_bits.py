def solution(numbers):
    answer = []
    for num in numbers:
        if num%2==0:
            temp = num+1
        else:
            n = '0' + str(bin(num)[2:])
            nv = n[::-1]
            for i in range(0, len(nv)):
                if nv[i] == '0':
                    temp = num + 2 ** (i - 1)
                    break
        answer.append(temp)
    return answer

#시간 초과
def solution2(numbers):
    answer = []
    for n in numbers:
        temp = n+1
        while(True):
            s = bin(n^temp)[2:]
            if(s.count('1')>=1 and s.count('1')<=2):
                answer.append(temp)
                break
            temp+=1
    return answer

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19]
print(solution(numbers))