def count(a):
    cnt1 = 0
    cnt0 = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                cnt0 += 1
            elif a[i][j] == 1:
                cnt1 += 1
    return [cnt0, cnt1]

def check(a):
    [cnt0, cnt1] = count(a)
    if cnt1 == 0 or cnt0 == 0:
        return True
    else:
        return False

def solution(arr):
    answer = [0,0]
    n = len(arr)
    while n>1:
        temp1 = []
        for i in range(0, n//2):
            t = []
            for j in range(0,n//2):
                t.append(arr[i][j])
            temp1.append(t)
        if check(temp1):
            [cnt0,cnt1] = count(temp1)
            answer[0] -= cnt0
            answer[1] -= cnt1
            return 
        else:
            solution(temp1)
        temp2 = []
        for i in range(0,n//2):
            t = []
            for j in range(n//2,n):
                t.append(arr[i][j])
            temp2.append(t)

        temp3 = []
        for i in range(n // 2, n):
            t = []
            for j in range(0, n // 2):
                t.append(arr[i][j])
            temp3.append(t)

        temp4 = []
        for i in range(n // 2,n):
            t = []
            for j in range(n // 2, n):
                t.append(arr[i][j])
            temp4.append(t)


    return answer

arr = [[1,1,0,0],[1,1,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))