changeL = {'A':(0,1), 'B':(0,2), 'C':(0,3),
         'D':(1,2), 'E':(1,3), 'F':(2,3)}
cup = ['sb','o','o','bb']

locate = input()
for l in locate:
    temp = cup[changeL[l][0]]
    cup[changeL[l][0]] = cup[changeL[l][1]]
    cup[changeL[l][1]] =temp
print(cup.index('sb')+1)
print(cup.index('bb')+1)