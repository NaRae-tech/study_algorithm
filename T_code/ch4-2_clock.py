import sys
N = int(sys.stdin.readline())
count = 0
for i in range(0,N+1):
    for j in range(0,60):
        for k in range(0,60):
            if(i==3 or j==3 or k==3):
                count+=1
            elif (i == 13 or j == 13 or k == 13):
                count += 1
            elif (i == 23 or j == 23 or k == 23):
                count += 1
            elif ((30<=i and i<=39) or (30<=j and j<=39) or (30<=k and k<=39)):
                count += 1
            elif (i == 43 or j == 43 or k == 43):
                count += 1
            elif (i == 53 or j == 53 or k == 53):
                count += 1
print(count)