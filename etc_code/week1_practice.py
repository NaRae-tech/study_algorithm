def intro_ex1():
    x=int(input())
    y=int(input())
    print("add: ",x+y, " sub: ", x-y, " mul: ",x*y, " div: ", x/y)

def intro_ex2():
    x=int(input())
    y=int(input())
    print("%d X %d = %d"%(x,y,x*y))

def intro_ex3():
    print("Please enter the number : ")
    x = int(input())
    for i in range(x-1,-1,-1):
        for j in range(i,-1,-1):
            print('*',end="")
        print('')

def intro_ex4():
    i = 1
    sum = 0
    while i<11:
        sum+=i
        print(i," --> ", sum)
        i+=1