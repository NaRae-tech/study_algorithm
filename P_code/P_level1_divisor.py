n = 12

print(n+sum([i for i in range(1, n//2+1) if n%i==0]))

divisor = []
for i in range(1,n+1):
    if(n%i==0):
        divisor.append(i)
print(sum(divisor))