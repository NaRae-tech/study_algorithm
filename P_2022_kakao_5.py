def solution(info, edges):
    answer = 0
    wolf = 0
    sheep = 0
    tree = {}
    for i in range(len(edges)):
        if edges[i][0] not in tree:
            tree[edges[i][0]] = [edges[i][1]]
        else:
            tree[edges[i][0]].append(edges[i][1])

    return answer


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))