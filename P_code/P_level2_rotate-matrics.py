from collections import deque
def solution(rows, columns, queries):
    answer = []
    matrics = [[columns*i+j for j in range(1,columns+1)]for i in range(rows)]

    for x,y,X,Y in queries:
        x1, y1, x2,y2 = x-1,y-1,X-1,Y-1
        temp = deque()
        for i in range(x1,x2):
            temp.append(matrics[i][y1])
        for i in range(y1,y2):
            temp.append(matrics[x2][i])
        for i in range(x2,x1,-1):
            temp.append(matrics[i][y2])
        for i in range(y2,y1,-1):
            temp.append(matrics[x1][i])
        answer.append(min(temp))
        temp.append(temp.popleft())

        for i in range(x1, x2):
            matrics[i][y1] = temp.popleft()
        for i in range(y1, y2):
            matrics[x2][i]= temp.popleft()
        for i in range(x2, x1, -1):
            matrics[i][y2]= temp.popleft()
        for i in range(y2, y1, -1):
            matrics[x1][i]= temp.popleft()

    return answer

rows = 6
columns = 6
queries = 	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))