arr=[3,2,6]
divisor = 10

#방법1
print(sorted([item for item in arr if(item%divisor==0)]) or [-1])

#방법2
answer = []
for item in arr:
    if(item%divisor==0):
        answer.append(item)
if(len(answer)==0):
    answer.append(-1)
print(sorted(answer))