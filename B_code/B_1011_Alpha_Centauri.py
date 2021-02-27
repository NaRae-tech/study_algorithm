import sys
T = int(input())
for t in range(0,T):
    X,Y = sys.stdin.readline().split()

    distance = int(Y)-int(X)    #이동해야 하는 거리
    count = 0                   #이동한 횟수
    move = 1                    #한 번 이동할 때 최대 이동 거리
    maxDisbycount = 0           #count별 이동 가능한 최대 distance
    while maxDisbycount < distance:
        count += 1
        maxDisbycount += move   #count 수에 해당하는 move를 더함
        if count % 2 == 0:      # count가 2의 배수일 때,
            move += 1
    print(count)