s = "AB"
n = 1

a=list(map(str,s))
for i in range(0, len(a)):
    if(a[i]==" "):
        pass
    elif(a[i].islower()):
        a[i] = chr(97+(ord(a[i])+n-97)%26)
    else:
        a[i] = chr(65+(ord(a[i])+n-65)%26)
print("".join(a))
