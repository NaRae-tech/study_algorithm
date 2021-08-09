def solution(n):
    num = ['1','2','4']
    answer = []
    while n>0:
        n-=1
        answer+=num[n%3]
        n//=3
    answer.reverse()
    return ''.join(answer)

def solution2(n):
    start=1
    length = 1
    while True:
        if start>n:
            length -= 1
            start-=3**length
            break
        else:
            start +=(3**length)
            length+=1
    print(start,length)

    c = ['1','2','4']
    difference = n-start
    difference_3 = []
    while difference>0:
        difference_3.append(int(difference%3))
        difference//=3
    while len(difference_3)<length:
        difference_3.append(0)
    difference_3.reverse()

    answer=""
    for i in range(len(difference_3)):
        answer+=c[difference_3[i]]
    return answer

n = 20
print(solution(n))