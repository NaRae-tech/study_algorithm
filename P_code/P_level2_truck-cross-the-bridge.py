def solution(bridge_length, weight, truck_weights):
    bridge = []
    time = 0
    index = 0
    while(index<len(truck_weights)):
        time+=1
        if len(bridge)>=bridge_length:
            del bridge[-1]
        if sum(bridge)+truck_weights[index] > weight:
            bridge.insert(0,0)
        else:
            bridge.insert(0, truck_weights[index])
            index+=1
    return time+bridge_length

#시간초과
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    time = 0
    index = 0
    while(index<len(truck_weights)):
        time += 1
        if len(bridge) >= bridge_length:
            bridge.pop()
        if sum(bridge) + truck_weights[index] > weight:
            bridge.appendleft(0)
        else:
            bridge.appendleft(truck_weights[index])
            index += 1
    return time + bridge_length

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length,weight,truck_weights))