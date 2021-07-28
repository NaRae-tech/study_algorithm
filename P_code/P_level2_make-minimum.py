A = [1, 4, 2]
B = [5,4,4]

#방법1
print(sum(a*b for a,b in zip(sorted(A), sorted(B,reverse=True))))

#방법2
A.sort()
B.sort()
answer = 0
for i in range(0, len(A)):
    answer+= (A[i]*B[-1-i])
print(answer)

#방법 3(시간초과)
answer = 0
for i in range(0,len(A)):
    answer+=(max(A)*min(B))
    print(max(A), min(B), answer)
    del A[A.index(max(A))]
    del B[B. index(min(B))]
