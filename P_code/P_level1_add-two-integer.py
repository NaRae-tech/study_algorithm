a = 5
b = 3

print((abs(a-b)+1)*(a+b)//2)

small = min(a,b)
big = max(a,b)
print(sum(i for i in range(small,big+1)))