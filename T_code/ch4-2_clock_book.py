import sys
N = int(sys.stdin.readline())
count =0
for i in range(0,N+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)