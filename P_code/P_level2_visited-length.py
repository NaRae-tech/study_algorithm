def solution(dirs):
    answer = 0
    x,y = 0,0
    direction = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    visited = set()
    for d in dirs:
        nx = x+direction[d][0]
        ny = y+direction[d][1]
        if (-5<= nx and nx<=5) and (-5<=ny and ny<=5):
            if (x,y,nx,ny) not in visited:
                visited.add((x,y,nx,ny))
                visited.add((nx,ny,x,y))
                answer+=1
                x,y = nx,ny
            else:
                x,y = nx,ny
    return answer

dirs="UUUUDUDUDUUU"
print(solution(dirs))