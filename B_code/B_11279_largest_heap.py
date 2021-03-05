import sys
import heapq
T = int(sys.stdin.readline())
heap = []
for _ in range(T):
    N = int(sys.stdin.readline())
    if(N==0):
        #힙이 0인지 확인후 최대값 출력 혹은 0출력
        if(len(heap)==0):
            print(0)
        else:
            print(heapq.heappop(heap)*(-1))
    else:
        #힙에 집어넣기
        heapq.heappush(heap,-N)