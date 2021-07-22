numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

answer = ''
phone = [[1,3],
         [0,0],[1,0],[2,0],
        [0,1],[1,1],[2,1],
        [0,2],[1,2],[2,2]]
L = [0,3]
R = [2,3]
for num in numbers:
   if(num==1 or num==4 or num==7):
       L = phone[num]
       answer+='L'
   elif(num==3 or num==6 or num==9):
       R=phone[num]
       answer+='R'
   else:
       distanceL = abs(phone[num][0]-L[0]) + abs(phone[num][1]-L[1])
       distanceR = abs(phone[num][0]-R[0]) + abs(phone[num][1]-R[1])
       if(distanceL<distanceR):
           answer+='L'
           L = phone[num]
       elif(distanceL>distanceR):
           answer+='R'
           R = phone[num]
       else:
           if(hand=="left"):
               answer+='L'
               L=phone[num]
           else:
               answer+='R'
               R=phone[num]

print(answer)