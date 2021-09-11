def solution(a,s):
    answer =[]
    before = 0
    after = 0
    for S in s:
        after += S
        b=[]
        for k in range(before, after):
            b.append([a[k]])
        before = after

        i = 0
        c = []
        n = len(b)
        while i!=n:
            if i-1<0:
                i+=1
            else:
                if sum(b[i]) == sum(b[i-1]):
                    b[i] += b[i-1]
                    del b[i-1]
                    c.append(i)
                else:
                    i+=1
            n = len(b)
        print(c)
    return answer

a = [1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6]
s = [4,3,1,5,6]
print(solution(a,s))