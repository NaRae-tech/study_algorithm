def solution(priorities, location):
    printer = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        current = printer.pop(0)
        if any(current[1]<item[1] for item in printer):
            printer.append(current)
        else:
            answer += 1
            if current[0] == location:
                break
    return answer


from collections import deque
def solution2(priorities, location):
    printer = deque(priorities)
    answer= 0
    while(True):
        if printer[0]>=max(printer):
            printer.popleft()
            answer += 1
            if location == 0:
                break
            else:
                location-=1
        else:
            printer.append(printer.popleft())
            if location == 0:
                location = len(printer)-1
            else:
                location-=1
        print(printer,location)
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))
