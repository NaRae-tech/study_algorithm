import heapq
def solution(scoville,K):
    answer =0
    scoville_heap = []
    for item in scoville:
        heapq.heappush(scoville_heap,item)
    while(True):
        temp = heapq.heappop(scoville_heap)
        if(temp>=K):
            break
        else:
            answer+=1
            if(len(scoville_heap)>0):
                temp2=heapq.heappop(scoville_heap)
                heapq.heappush(scoville_heap,temp+temp2*2)
            else:
                return -1
    return answer

scoville =[1,2,3,9,10,12]
print(solution(scoville, 7))