import math
sugar = int(input())
kg5 = 0
max5 = math.floor(sugar/5)
kg3 = 0
max3 = math.floor(sugar/3)

minimum = max5+max3
finish = False
for i in range(max5,-1,-1):
    kg5 = i
    if(sugar==5*kg5 + 3*kg3):
        if(kg5+kg3<=minimum):
            minimum = kg5+kg3
            finish = True
        break
    for j in range(0,max3+1):
        kg3 = j
        if (sugar == 5 * kg5 + 3 * kg3):
            if (kg5 + kg3 <= minimum):
                minimum = kg5 + kg3
                finish = True
            break

if(finish == True):
    print(minimum)
else:
    print(-1)
