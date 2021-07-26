n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]

#방법1
answer = []
for i in range(0,n):
    answer.append(str(bin(arr1[i]|arr2[i])[2:]).zfill(n)
                  .replace('1','#').replace('0',' '))
print(answer)

#방법 2
map1 = []
map2 = []
for i in range(0,n):
    map1.append(list(map(int,format(arr1[i],"b").zfill(n))))
    map2.append(list(map(int, format(arr2[i], "b").zfill(n))))
print(map1)
print(map2)

result = []
for i in range(0,n):
    temp=""
    for j in range(0,n):
        if(map1[i][j] or map2[i][j]):
            temp+="#"
        else:
            temp+=" "
    result.append(temp)
print(result)