def isIt(numbers, left, right, mid, wantfind):
    if(numbers[mid]<wantfind):
        if(left==mid or mid == right):
            return 0
        return isIt(numbers,mid,right,(mid+right)//2,wantfind)
    elif(numbers[mid]>wantfind):
        if (left == mid or mid == right):
            return 0
        return isIt(numbers, left,mid,(left+mid)//2,wantfind)
    elif(numbers[mid]==wantfind):
        return 1
import sys
M = int(sys.stdin.readline())
numbers= list(map(int,sys.stdin.readline().split()))
numbers = sorted(numbers)

N = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))

#targe N개의 존재여부를 찾음
for i in range(0,N):
    #아예 범위 안에 없는 수인지 확인
    if(numbers[0]>target[i] or numbers[M-1]<target[i]):
        print(0)
    #경계 선 확인
    elif (numbers[0]==target[i] or numbers[M-1]==target[i]):
        print(1)
    #경계선 안 확인
    else:
        print(isIt(numbers, 0,M-1,M//2,target[i]))