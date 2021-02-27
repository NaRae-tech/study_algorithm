import sys
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
answer = [-1 for _ in range(N)]
stack = [0]

i = 1
while(stack and i<N):
    while(stack and (numbers[stack[-1]]<numbers[i])):
        answer[stack[-1]] = numbers[i]
        stack.pop()
    stack.append(i)
    i+=1

for item in answer:
    print(item, end = ' ')