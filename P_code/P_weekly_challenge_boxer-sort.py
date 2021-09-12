import math
def solution(weights, head2head):
    answer = []

    boxer = {}
    people = len(weights)
    for i in range(people):
        win = 0
        loose = 0
        bigger = 0
        for j in range(people):
            if head2head[i][j] == "W":
                win+=1
                if weights[i]<weights[j]:
                    bigger+=1
            elif head2head[i][j]=="L":
                loose+=1
            else:
                continue
        rate = (win/(win+loose))*100 if win+loose!=0 else (win/1)*100
        boxer[i] = [rate, bigger, weights[i]]
    boxer = boxer.items()
    boxer = sorted(boxer, key=lambda x:(-x[1][0], -x[1][1], -x[1][2], x[0]))

    for b in boxer:
        answer.append(b[0]+1)
    return answer

weights = [50,82,75,120]
head2head = 	["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights, head2head))