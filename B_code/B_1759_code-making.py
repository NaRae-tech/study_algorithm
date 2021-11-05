import itertools
l,c = list(map(int,input().split(' ')))
alpha = list(input().split(' '))

alpha = sorted(alpha)
print(alpha)
codes = list(itertools.combinations(alpha,l))
print(codes)
for code in codes:
    cntV,cntC = 0,0
    for c in code:
        if c in ['a','e','i','o','u']:
            cntV +=1
    cntC = l-cntV
    if cntV>=1 and cntC>=2:
        print(''.join(code))

