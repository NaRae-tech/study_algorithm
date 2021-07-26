s = "hello world "

#방법 1
print(" ".join(map(lambda x:"".join([a.lower() if i%2 else a.upper() for i,a in enumerate(x)]), s.split(" "))))

#방법 2
a = list(map(list,s.lower().split(" ")))
b= []
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        if(j%2==0 and a[i][j]!=" "):
            a[i][j] = chr(ord(a[i][j])-32)
    b.append(''.join(a[i]))
print(' '.join(b))