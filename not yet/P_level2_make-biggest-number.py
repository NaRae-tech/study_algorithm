def solution(number, k):
    answer = []
    for i in range(len(number)):
        if k<0:
            answer.append(number[i])
        else:
            if (not answer) or (answer[-1]>=number[i]):
                answer.append(number[i])
            else:
                for j in range(len(answer)):
                    if answer[-1]<number[i] and k>0:
                        answer.pop()
                        k-=1
                answer.append(number[i])
            print(number[i], answer)
    answer = list(map(str,answer))
    return "".join(answer)

number = "4177252841"
k = 4
print(solution(number,k))