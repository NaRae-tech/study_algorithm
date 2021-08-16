def solution(place):
    answer =[]
    for room in place:
        person = []
        for i in range(0,5):
            for j in range(0,5):
                if room[i][j] == "P":
                    person.append([i,j])
        flag = True
        for i in range(len(person)):
            for j in range(i+1,len(person)):
                if (abs(person[i][0]-person[j][0])+abs(person[i][1]-person[j][1]))<=2:
                    if person[i][0]==person[j][0]:
                        if room[person[i][0]][(person[i][1]+person[j][1])//2]!="X":
                            flag = False
                            break
                    elif person[i][1] == person[j][1]:
                        if room[(person[i][0]+person[j][0])//2][person[i][1]]!="X":
                            flag = False
                            break
                    elif person[i][0]+1 == person[j][0] and person[i][1]+1 == person[j][1]:

                        if not(room[person[i][0]][person[j][1]]=="X" and room[person[j][0]][person[i][1]]=="X"):
                            flag = False
                            break
                    elif person[i][0] +1== person[j][0] and person[i][1] == person[j][1]+1:
                        if not(room[person[j][0]][person[i][1]]=="X" and room[person[i][0]][person[j][1]]=="X"):
                            flag = False
                            break
                    else:
                        flag = False
                        break

            if flag==False:
                break
        answer.append(int(flag))
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))