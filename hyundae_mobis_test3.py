from itertools import combinations
def solution(m, b):
    answer = []
    index = 0

    for M in m:
        a = b[index:index + M]
        a = sorted(a)
        index+=M
        flag = False
        minimum = 2^30
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                bitwise = a[i] & a[j]
                print(a[i], a[j], bitwise)
                if bitwise == 0:
                    minimum = 0
                    flag = True
                    break
                elif minimum>bitwise:
                    minimum=bitwise
            if flag==True: break
        answer.append(minimum)
    return answer

m = [2,3,4]
b = [30,29,2,4,5,6,7,8,9]
print(solution(m,b))