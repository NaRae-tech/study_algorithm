from collections import deque
def solution(prices):
    answer =[0]
    stack = deque(prices)

    mini = stack.pop()
    miniInd = len(stack)-1


    return answer
prices = [3,1,2,1,3,3,2,3,1]
print(solution(prices))