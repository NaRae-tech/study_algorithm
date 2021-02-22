import sys
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if(num == 0):
        del numbers[0]
    else :
        numbers.insert(0,num)
result =0
for i in range(len(numbers)):
    result += numbers[i]
print(result)