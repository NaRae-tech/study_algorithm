n = 12345

#방법 1
s = list(reversed(str(n)))
answer = []
for item in s:
    answer.append(int(item))
print(answer)

#방법 2
list(map(int, reversed(str(n))))