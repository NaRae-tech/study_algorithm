def isIt(numbers, left,right, mid, target):
    if(numbers[mid]<target):
        if(left==mid or right==mid):
            return -1
        return isIt(numbers, mid,right,(mid+right)//2,target)
    elif(numbers[mid]>target):
        if (left == mid or right == mid):
            return -1
        return isIt(numbers,left,mid,(left+mid)//2,target)
    elif(numbers[mid]==target):
        return mid
import sys
from collections import Counter
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
#같은 수가 몇개씩 있는지 count
counterNumbers = Counter(numbers)
#중복을 없애고 오름차순으로 정렬
numbers = sorted(list(set(numbers)))

M = int(sys.stdin.readline())
targetN = list(map(int,sys.stdin.readline().split()))
howmany = [0 for _ in range(M)]

for i in range(M):
    if(targetN[i]>numbers[len(numbers)-1] or targetN[i]<numbers[0]):
        howmany[i] = 0
    elif (targetN[i]==numbers[len(numbers)-1]):
        howmany[i] = counterNumbers[numbers[len(numbers)-1]]
    elif(targetN[i]<numbers[0]):
        howmany[i] = counterNumbers[numbers[0]]
    else:
        result = isIt(numbers, 0,len(numbers)-1,(len(numbers)-1)//2,targetN[i])
        if(result != -1):
            howmany[i] = counterNumbers[numbers[result]]

for item in howmany:
    print(item, end= " ")