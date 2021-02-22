numbers = []
def pop():
    del numbers[0]
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if(num==0):
        pop()
    else:
        numbers.insert(0,num)
result =0
for i in range(len(numbers)):
    result+=numbers[i]
print(result)