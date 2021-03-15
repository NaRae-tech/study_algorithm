turn = ['X',1,2,3,4,5,6,7,8,9]
position = [0,0,0,0,0,0,0,0,0,0]
def check():
    flag = False
    for i in range(1,4):
        # 세로 만족 경우
        if(position[i]==position[3+i]==position[6+i]):
            flag = True
            return position[i]
    #가로 만족 경우
    for i in range(0,3):
        if(position[1+3*i]==position[2+3*i]==position[3+3*i]):
            flag = True
            return position[1+3*i]
    #좌측대각선
    if(position[1]==position[5]==position[9]):
        flag = True
        return position[1]
    elif(position[3]==position[5]==position[7]):
        flag = True
        return position[3]
    if(flag==False):
        return 0

def printing():
    for i in range(0, 3):
        print(turn[1 + 3 * i],end=' ')
        print(turn[2 + 3 * i], end =' ')
        print(turn[3 + 3 * i])

checkingFlag = False
for i in range(9):
    p1 = int(input())
    position[p1] = 1
    turn[p1] = 'X'
    if(check()==1 or check()==2):
        printing()
        checkingFlag= True
        print("Win player is : player", check())
        break
    p2 = int(input())
    position[p2] = 2
    turn[p2] = 'O'
    if (check() == 1 or check() == 2):
        printing()
        checkingFlag = True
        print("Win player is : player", check())
        break
if(checkingFlag==False):
    printing()
    print("Win player is none")