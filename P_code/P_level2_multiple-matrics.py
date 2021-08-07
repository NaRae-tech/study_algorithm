def solution(arr1,arr2):
    answer = [[ 0 for i in range(len(arr2[0]))]for j in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            for k in range(len(arr1[0])):
                print(i,j,k, arr1[i][k], arr2[k][j])
                answer[i][j] += (arr1[i][k]* arr2[k][j])
    return answer

arr1 =  [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]
print(solution(arr1,arr2))
