T = int(input())
for i in range(1,T+1):
    A,B = input().split()
    sum = str(int(A)+int(B))
    print("Case #"+str(i)+": "+A+" + "+B+" = "+sum)
