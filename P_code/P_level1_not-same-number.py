arr = [4,4,4,3,3]

result =[]
for item in arr:
    if(len(arr)==0 or result[-1]!=item):
        result.append(item)
print(result)

result = []
for item in arr:
    if(result[-1:]!=[item]):
        result.append(item)
print(result)

now = arr[0]
answer = [now]
for item in arr:
    if(item!=now):
        answer.append(item)
        now=item
print(answer)
