def solution(n):
    return bin(n).count('1')

def solution2(n):
    answer = 0
    while n>0:
        if n%2==1:
            answer+=1
            n-=1
        else:
            n//=2
    return answer

n = 5000
print(solution(n))