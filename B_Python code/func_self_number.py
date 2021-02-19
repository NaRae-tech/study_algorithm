list_nsn = [1 for t in range(0,10001)]

def NotselfNumber(a:int):
    new_a = a
    for i in range(0, len(str(a))):
        new_a += int(str(a)[i])
    if (new_a<10000):
        list_nsn[new_a] =0
        return NotselfNumber(new_a)
    else:
        return

for j in range(1,10001):
    NotselfNumber(j)

for k in range(1,10000):
    if(list_nsn[k]==1):
        print(k)
