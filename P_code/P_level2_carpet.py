brown = 8
yellow = 1

answer = []
for m in range(1, yellow+1):
    n = int(brown/2 -2 -m)
    if(n*m == yellow):
        col = m+2
        row = n+2
        answer.append(row)
        answer.append(col)
        break

print(answer)