def cond_ex1():
    print("a = ", end="")
    pointA = list(map(int,input().replace("(","").replace(")","").split(",")))
    print("b = ", end="")
    pointB = list(map(int,input().replace("(","").replace(")","").split(",")))

    if pointA == pointB:
        print("same points")
    elif pointA[0] == pointB[0] and pointA[1] == -1*pointB[1]:
        print("Y-axis symmetry")
    elif pointA[1] == pointB[1] and pointA[0] == -1*pointB[0]:
        print("X-axis symmetry")
    elif pointA[0]*-1 == pointB[0] and pointA[1]*-1==pointB[1]:
        print("Origin symmetry")
    else:
        print("Nothing")

def cond_ex2():
    print("time = ",end="")
    time = list(map(int,input().split(":")))
    changeTime = []
    if time[1]>=30:
        changeTime.append(str(time[0]).zfill(2))
        changeTime.append(str(time[1]-30).zfill(2))
    else:
        changeTime.append(str((time[0]-1+24)%24).zfill(2))
        changeTime.append(str(time[1] +60 - 30).zfill(2))
    print("%s:%s" % (changeTime[0], changeTime[1]))

def cond_ex3():
    print("player1 = ",end="")
    player1 = input()
    print("player2 = ",end="")
    player2 = input()

    case = {"rock":0, "paper":1, "scissors":2}
    p1,p2 = case[player1], case[player2]
    if p2 == p1:
        print("same")
    elif p2-p1==1 or p2-p1==-2:
        print("player2")
    else:
        print("player1")

def loop_ex1():
    print("1: Insert coin | 2: Item list | 3: Select fruit | 4: Change money | Q: exit")
    print("Please select menu: ", end="")
    menu = input()
    price = 0
    canChoice = [["orange",300], ["shine muscat",1000]]
    while menu != "Q":
        if menu=="1":
            print("How much money do you want to put in?", end="")
            price += int(input())
            print("You insert %d coins" %price)
        elif menu == "2":
            print(":" * 4, "1. Orange : 300", ":" * 4, end=" ")
            print(":" * 4, "2. Shine muscat : 1000", ":" * 4)
        elif menu == "3":
            print("Which fruit do you want?",  end=" ")
            choice = int(input())-1
            if price >= canChoice[choice][1]:
                print("You get an %s"%canChoice[choice][0])
                price -= canChoice[choice][1]
                print("You have %d coins"%price)
            else:
                print("You can't get an %s" % canChoice[choice][0])
        elif menu == "4":
            print("You get %d conis back" %price)
            price-=price

        print("\n1: Insert coin | 2: Item list | 3: Select fruit | 4: Change money | Q: exit")
        print("Please select menu: ", end="")
        menu = input()
        print("")

def loop_ex2():
    num = list(map(int, input().replace("[","").replace("]","").split(", ")))
    mean = sum(num)/len(num)
    variance = 0
    for n in num:
        variance += (n-mean)**2
    variance /= len(num)
    print("Means : {:.1f}".format(mean))
    print("Variance : {:.1f}".format(variance))

def loop_ex3():
    student = list(map(int, input().replace("[","").replace("]","").split(",")))
    for i in range(len(student)):
        grade = ""
        if student[i] in range(90,101):
            grade = "A"
        elif student[i] in range(80,90):
            grade = "B"
        elif student[i] in range(70,80):
            grade = "C"
        elif student[i] in range(60,70):
            grade = "D"
        else:
            grade="F"
        print("%d번 학생은 %d점으로 %s입니다."%(i+1, student[i], grade))

def loop_ex4():
    print("a = ",end="")
    a = list(map(int, input().replace("[","").replace("]","").split(", ")))
    maximum = max(a)
    check = [True for i in range(maximum+1)]
    for i in range(2,maximum//2+1):
        for j in range(i+i, maximum+1, i):
            if check[j] == True:
                check[j] = False
    prime = []
    composite = []
    for n in a:
        if check[n] == False:
            composite.append(n)
        else:
            prime.append(n)
    print("Prime numbers : ", prime,  len(prime))
    print("Composite_numbers : ", composite, len(composite))

def loop_ex5():
    l = [[1, 2], [5, 4], [6, 6], [7, 8], [9, 10]]
    """
    newone = []
    for i in range(len(l)):
        newone.extend(l[i])
    """
    newone = [j for i in l for j in i]
    return newone
